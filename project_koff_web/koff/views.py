from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .models import Category, BusinessEntity
from django.db.models import Avg
from .serializers import CategorySerializer, BusinessEntitySerializer, BusinessEntityDetailSerializer, BusinessEntitySearchSerializer
from datetime import datetime

from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D

from drf_haystack.viewsets import HaystackViewSet


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


class BusinessEntityDetail(mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    """
    Retrieves a category
    """
    queryset = BusinessEntity.objects.all()
    serializer_class = BusinessEntityDetailSerializer


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
        lat = float(location[0])
        lon = float(location[1])
        radius = float(self.request.query_params.get('radius', None))
        queryset = BusinessEntity.objects.filter(
            active=True,
            categories__in=[int(subcategory_pk)],
            location__distance_lte=(
                Point(lat, lon),
                D(km=radius)
            )
        )

        is_working_time = int(self.request.query_params.get('is_working', None))

        if(is_working_time == 1):
            print("Day name %s" % (datetime.now().strftime('%a')))
            print("Time %s" % (datetime.now().time()))
            queryset = queryset.filter( # return only those that are working now
                workinghours__name__in=[datetime.now().strftime('%a')], # returns current day in short format (Mon, Tue)
                workinghours__start_time__lte=datetime.now().time(),
                workinghours__end_time__gte=datetime.now().time()
            )

        # Get distance from provided location to BusinessEntity location
        dist = Distance('location', Point(lat, lon, srid=4326))
        queryset = queryset.annotate(distance=dist)

        # Get average rating for every BusinessEntity
        queryset = queryset.annotate(avg_rating=Avg('rating__rating'))

        if(sort_mode == 'distance' or sort_mode is None):
            queryset = queryset.order_by('distance')
        elif (sort_mode == 'rating_asc'):
            queryset = queryset.order_by('avg_rating')
        elif (sort_mode == 'rating_desc'):
            queryset = queryset.order_by('-avg_rating')
        elif (sort_mode == 'a_z'):
            queryset = queryset.order_by('name')
        elif (sort_mode == 'z_a'):
            queryset = queryset.order_by('-name')

        return queryset


@api_view(['GET'])
def validate_token(request):
    return Response({"detail": "Valid token."})

class BusinessEntitySearchView(HaystackViewSet):
    index_models = [
        BusinessEntity
    ]
    serializer_class = BusinessEntitySearchSerializer
    pagination_class = BusinessEntitiesPagination
