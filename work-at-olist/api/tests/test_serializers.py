from django.test import TestCase
from api import models, serializers


def create_category(channel, category, parent_category):

    return models.Category.objects.update_or_create(
            name=category,
            parent=parent_category,
            channel=channel
        )


class ChannelSerializerTest(TestCase):

    def test_create(self):
        expected = {'name': 'test'}

        channel = models.Channel.objects.create(name='test')
        serializer = serializers.ChannelSerializer(
            channel, context={'request': None}
        )

        self.assertEqual(serializer.data, expected)


class CategoriesSerializerTest(TestCase):

    def test_create(self):
        expected = {
            "name": "Auto",
            "children": [
                {
                    "name": "Cars",
                    "children": []
                }
            ]
        }

        channel = models.Channel.objects.create(name='test_categories')
        parent_category, _ = create_category(channel, "Auto",
                                             None)
        category, _ = create_category(channel, "Cars", parent_category)
        serializer = serializers.CategoriesSerializer(
            parent_category, context={'request': None}
        )

        self.assertEqual(serializer.data, expected)
