from rest_framework import viewsets, generics
from api import models
from api import serializers


class ChannelListViewSet(viewsets.ModelViewSet):
    queryset = models.Channel.objects.all()
    serializer_class = serializers.ChannelSerializer


class ChannelListCategories(generics.ListAPIView):
    serializer_class = serializers.CategoriesSerializer

    def get_queryset(self):
        channel = models.Channel.objects.filter(name=self.kwargs['name'])
        return models.Category.objects.filter(channel=channel,
                                              level=0)


class CategoriesView(generics.ListAPIView):
    serializer_class = serializers.CategoriesSerializer

    def get_queryset(self):
        return models.Category.objects.filter(
            name=self.kwargs['name']).get_ancestors(include_self=False)
