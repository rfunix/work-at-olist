from rest_framework import viewsets
from workatolist import models
from api import serializers


class ChannelListViewSet(viewsets.ModelViewSet):
    queryset = models.Channel.objects.all()
    serializer_class = serializers.ChannelSerializer
