from rest_framework import serializers
from .models import Category, BusinessEntity
from rest_framework_recursive.fields import RecursiveField


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


class DistanceField(serializers.Field):

    def to_representation(self, obj):
        return "%.9f" % (obj.m)


class LocationField(serializers.Field):

    def to_representation(self, obj):
        return "%.6f, %.6f" % (obj.x, obj.y)


class BusinessEntitySerializer(serializers.ModelSerializer):
    distance = DistanceField()
    location = LocationField()

    class Meta:
        model = BusinessEntity

        fields = ('pk', 'name', 'address', 'distance', 'location')
        read_only_fields = ('pk', 'name', 'address', 'distance', 'location')
