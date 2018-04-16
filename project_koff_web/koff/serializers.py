from rest_framework import serializers
from .models import Category
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
        fields = ('pk', 'name', 'children')
        read_only_fields = ('pk', 'name', 'children')