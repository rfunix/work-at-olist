from django.test import TestCase
from api import models

def create_channel(name):

    return models.Channel.objects.create(name=name)

def create_category(channel, category, parent_category):

    return models.Category.objects.update_or_create(
            name=category,
            parent=parent_category,
            channel=channel
        )

class ChannelTest(TestCase):

    def test_str(self):

        name = 'test_channel'
        channel = create_channel(name)
        self.assertEqual(channel.__str__(), name)

class CategoryTest(TestCase):

    def test_str(self):

        channel_name = 'test_channel_category'
        parent_category_name = 'test_category_parent'
        category_name = 'test_category'

        channel = create_channel(channel_name)

        parent_category, _ = create_category(channel, parent_category_name,
                                             None)
        category, _ = create_category(channel, category_name, parent_category)

        self.assertEqual(category.__str__(),
                         "%s:%s:%s" % (channel_name,
                                       category_name,
                                       parent_category_name))
