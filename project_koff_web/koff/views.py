from rest_framework import viewsets, mixins, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .models import Category, BusinessEntity, RatingAndComment
from django.db.models import Avg, Q, Case, Count, When, IntegerField, Value
from django.db.models.functions import Coalesce
from django.conf import settings
from .serializers import CategorySerializer, BusinessEntitySerializer, BusinessEntityDetailSerializer, BusinessEntitySearchSerializer, RatingAndCommentSerializer, RatingAndCommentPostSerializer, TokenSerializer
from datetime import datetime

from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D

from drf_haystack.viewsets import HaystackViewSet
from itertools import chain
from rest_framework.decorators import detail_route, list_route

from rest_framework.authtoken.models import Token

import operator
import googlemaps 


class CategoryList(mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
    Lists categories
    """
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = CategorySerializer
    #pagination_class = None


class CategoryDetail(mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    Retrieves a category
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TokenDetail(mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    Retrieves a category
    """
    queryset = Token.objects.all()
    serializer_class = TokenSerializer


class BusinessEntityDetail(mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    """
    Retrieves details of a BusinessEntity
    """
    queryset = BusinessEntity.objects.all()
    serializer_class = BusinessEntityDetailSerializer


class RatingAndCommentPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


class RatingsAndComments(generics.ListAPIView,
                        viewsets.GenericViewSet):
    """
    Lists comments and ratings for a BusinessEntity
    """

    serializer_class = RatingAndCommentSerializer
    pagination_class = RatingAndCommentPagination

    def get_queryset(self):
        businessentity_pk = self.request.query_params.get('entity', None)
        user_queryset = RatingAndComment.objects.filter(
            user=self.request.user,
            entity=businessentity_pk
        ).annotate(weight=Value(0, IntegerField()))
        queryset = RatingAndComment.objects.filter(
            ~Q(user=self.request.user),
            entity=businessentity_pk
        ).annotate(weight=Value(1, IntegerField()))
        total_qs = user_queryset.union(queryset).order_by('weight', 'updated_at')
        return total_qs


class RatingsAndCommentsList(generics.ListCreateAPIView):
    queryset = RatingAndComment.objects.all()
    serializer_class = RatingAndCommentPostSerializer


class RatingsAndCommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RatingAndComment.objects.all()
    serializer_class = RatingAndCommentSerializer


class BusinessEntitiesPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


class BusinessEntities(generics.ListAPIView,
                       viewsets.GenericViewSet):
    """
    Lists business entities
    """
    serializer_class = BusinessEntitySerializer
    pagination_class = BusinessEntitiesPagination

    def get_queryset(self):
        sort_mode = self.request.query_params.get('sort', None)
        subcategory_pk = self.request.query_params.get('subcategory', None)
        location = self.request.query_params.get('location', None).split(',')
        try:
            ids = self.request.query_params.get('ids', None).split(',')
        except AttributeError:
            ids = []

        lat = float(location[0])
        lon = float(location[1])
        radius = float(self.request.query_params.get('radius', None))

        queryset = BusinessEntity.objects.filter(
            active=True,
            location__distance_lte=(
                Point(lat, lon),
                D(km=radius)
            )
        )

        if ids:
            queryset = queryset.filter(id__in=ids)

        if subcategory_pk:
            queryset = queryset.filter(categories__in=[int(subcategory_pk)])

        is_working_time = int(self.request.query_params.get('is_working', None))

        days_eng_to_hr = {
            'Mon': 'Pon',
            'Tue': 'Uto',
            'Wed': 'Sri',
            'Thu': 'Čet',
            'Fri': 'Pet',
            'Sat': 'Sub',
            'Sun': 'Ned',
        }

        if(is_working_time == 1):
            print("Day name %s" % (datetime.now().strftime('%a')))
            print("Time %s" % (datetime.now().time()))
            queryset = queryset.filter( # return only those that are working now
                workinghours__name__in=[days_eng_to_hr[datetime.now().strftime('%a')]], # returns current day in short format (Mon, Tue)
                workinghours__start_time__lte=datetime.now().time(),
                workinghours__end_time__gte=datetime.now().time()
            )

        # Get distance from provided location to BusinessEntity location
        gmaps = googlemaps.Client(
            key=settings.GOOGLE_API_KEY
        )
        dist = Distance('location', Point(lat, lon, srid=4326))
        queryset = queryset.annotate(distance=dist)

        # Get average rating for every BusinessEntity
        queryset = queryset.annotate(avg_rating=Coalesce(Avg('ratingandcomment__rating'), 0))

        if (sort_mode == 'rating_asc'):
            queryset = queryset.order_by('avg_rating')
        elif (sort_mode == 'rating_desc'):
            queryset = queryset.order_by('-avg_rating')
        elif (sort_mode == 'a_z'):
            queryset = queryset.order_by('name')
        elif (sort_mode == 'z_a'):
            queryset = queryset.order_by('-name')

        for item in queryset:
            distance_matrix = gmaps.distance_matrix(origins=(lat, lon), destinations=(item.location.x,item.location.y))
            res = distance_matrix['rows'][0]['elements'][0]['distance']['value']
            item.distance.m = res

        if(sort_mode == 'distance' or sort_mode is None):
            queryset = sorted(queryset, key=operator.attrgetter('distance.m'))

        return queryset


@api_view(['GET'])
def validate_token(request):
    return Response({"detail": "Valid token."})

@api_view(['GET'])
def get_user_pk(request):
    return Response({"user_pk": request.user.pk})

@api_view(['GET'])
def get_user_comment_and_rating(request):
    businessentity_pk = request.query_params.get('entity', None)
    queryset = RatingAndComment.objects.filter(
        user=request.user,
        entity=businessentity_pk
    )
    if(queryset.exists()):
        result = queryset[0]
        return Response(
            {
                "pk": result.pk,
                "user_rating": result.rating,
                "user_comment": result.comment
            }
        )
    else:
        return Response(
            {
                "pk": -1,
                "user_rating": -1,
                "user_comment": ""
            }
        )

class BusinessEntitySearchView(HaystackViewSet):
    index_models = [
        BusinessEntity
    ]
    serializer_class = BusinessEntitySearchSerializer
