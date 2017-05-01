from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api import models


class BaseViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        channel = models.Channel.objects.create(name='test')
        parent = models.Category.objects.create(name='Auto', channel=channel,
                                                parent=None)
        models.Category.objects.create(name="Cars", channel=channel,
                                       parent=parent)


class ChannelListViewSetTest(BaseViewTest):

    def test_list_channels(self):
        response = self.client.get('/api/channels/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class ChannelListCategoriesViewSetTest(BaseViewTest):

    def test_list_categories(self):
        response = self.client.get('/api/channel-categories/test/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data[0]), 2)


class CategoriesViewTest(BaseViewTest):

    def test_categories(self):
        response = self.client.get('/api/category/Cars/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data[0]), 2)
