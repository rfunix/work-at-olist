from rest_framework import serializers
from workatolist import models


class ChannelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Channel
        fields = ('id', 'name')
