from rest_framework import serializers
from .models import Category, BusinessEntity, WorkingHours, RatingAndComment
from rest_framework_recursive.fields import RecursiveField
from .search_indexes import BusinessEntityIndex
from drf_haystack.serializers import HaystackSerializer
from rest_framework.authtoken.models import Token
from project_koff_web.users.serializers import UserSerializer


class DistanceField(serializers.Field):

    def to_representation(self, obj):
        return obj.m


class LocationField(serializers.Field):

    def to_representation(self, obj):
        return (obj.x, obj.y)

class UserDetailsField(serializers.Field):

    def to_representation(self, obj):
        return (obj.first_name, obj.last_name, obj.username, obj.pk)

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


class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Token
        fields = ('key', 'user')


class RatingAndCommentSerializer(serializers.ModelSerializer):
    user = UserDetailsField()
    created_at = serializers.DateTimeField(format="%d/%m/%y")
    updated_at = serializers.DateTimeField(format="%d/%m/%y")

    class Meta:
        model = RatingAndComment
        fields = ('pk', 'user', 'rating', 'comment', 'created_at', 'updated_at')


class RatingAndCommentPostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = RatingAndComment
        fields = ('pk', 'user', 'entity', 'rating', 'comment', 'created_at', 'updated_at')


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

        fields = ('pk', 'name', 'address', 'location', 'description', 'working_hours', 'e_mail', 'web_site', 'telephone_numbers', 'social_references', 'rating')
        read_only_fields = ('pk', 'name', 'address', 'location', 'description', 'working_hours', 'e_mail', 'web_site', 'telephone_numbers', 'social_references', 'rating')


class BusinessEntitySearchSerializer(HaystackSerializer):

    class Meta:
        model = BusinessEntity
        index_classes = [
            BusinessEntityIndex
        ]

        fields = ('id', 'name', 'description')
        read_only_fields = ('id', 'name', 'description')
