from rest_framework import serializers
from api import models
from rest_framework_recursive.fields import RecursiveField


class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Channel
        fields = ('name', 'slug')


class CategoriesSerializer(serializers.ModelSerializer):
    children = RecursiveField(required=True, allow_null=True, many=True)

    class Meta:
        model = models.Category
        fields = ('name', 'slug', 'children')
