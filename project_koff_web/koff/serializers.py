from rest_framework import serializers
from .models import Category, BusinessEntity, WorkingHours
from rest_framework_recursive.fields import RecursiveField
from .search_indexes import BusinessEntityIndex
from drf_haystack.serializers import HaystackSerializer


class DistanceField(serializers.Field):

    def to_representation(self, obj):
        return obj.m


class LocationField(serializers.Field):

    def to_representation(self, obj):
        return (obj.x, obj.y)


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.ListField(
        read_only=True,
        source='get_children',
        child=RecursiveField()
    )

    class Meta:
        model = Category
        depth = 1

        fields = ('pk', 'name', 'image', 'children')
        read_only_fields = ('pk', 'name', 'image', 'children')


class WorkingHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingHours
        fields = ('name', 'start_time', 'end_time')


class BusinessEntitySerializer(serializers.ModelSerializer):
    distance = DistanceField()
    location = LocationField()
    avg_rating = serializers.FloatField()
    working_hours = WorkingHoursSerializer(
        source='workinghours_set',
        many=True
    )

    class Meta:
        model = BusinessEntity

        fields = ('pk', 'name', 'address', 'distance', 'location', 'avg_rating', 'working_hours')
        read_only_fields = ('pk', 'name', 'address', 'distance', 'location', 'avg_rating', 'working_hours')


class BusinessEntityDetailSerializer(serializers.ModelSerializer):
    location = LocationField()
    working_hours = WorkingHoursSerializer(
        source='workinghours_set',
        many=True
    )

    class Meta:
        model = BusinessEntity

        fields = ('pk', 'name', 'address', 'location', 'description', 'working_hours', 'e_mail', 'web_site', 'telephone_references', 'social_references')
        read_only_fields = ('pk', 'name', 'address', 'location', 'description', 'working_hours', 'e_mail', 'web_site', 'telephone_references', 'social_references')


class BusinessEntitySearchSerializer(HaystackSerializer):

    class Meta:
        model = BusinessEntity
        index_classes = [
            BusinessEntityIndex
        ]

        fields = ('id', 'name', 'description')
        read_only_fields = ('id', 'name', 'description')
