from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'channels', views.ChannelListViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^channel-categories/(?P<name>\w+)/$',
        views.ChannelListCategories.as_view()),
    url(r'^category/(?P<name>\w+)/$', views.CategoriesView.as_view())
]
