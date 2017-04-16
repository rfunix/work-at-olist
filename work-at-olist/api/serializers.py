from rest_framework import serializers
from workatolist import models
from rest_framework_recursive.fields import RecursiveField


class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Channel
        fields = ('id', 'name')


class CategoriesSerializer(serializers.ModelSerializer):
    parent = RecursiveField(allow_null=True)

    class Meta:
        model = models.Category
        fields = ('name', 'parent')
