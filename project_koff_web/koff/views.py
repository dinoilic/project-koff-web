from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, BusinessEntity
from django.db.models import Avg
from .serializers import CategorySerializer, BusinessEntitySerializer

from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D


class CategoryList(mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
    Lists categories
    """
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = CategorySerializer


class CategoryDetail(mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    Retrieves a category
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BusinessEntities(generics.ListAPIView,
                       viewsets.GenericViewSet):
    """
    Lists business entities
    """
    serializer_class = BusinessEntitySerializer

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
