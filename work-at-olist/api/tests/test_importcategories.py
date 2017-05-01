import tempfile
import csv
from django.core.management import call_command
import os
from api import models
from django.test import TestCase


def create_tempcsv_file(file_content):

    csv_file = tempfile.NamedTemporaryFile(mode='w', delete=False)

    header_fields = ["Category"]
    csv_writer = csv.DictWriter(csv_file, fieldnames=header_fields)

    csv_writer.writeheader()

    for categories in file_content:
        csv_writer.writerow({"Category": categories})

    file_name = csv_file.name
    csv_file.close()

    return file_name


class ImportCategoriesTest(TestCase):
    categories = [
            "Books",
            "Books / National Literature",
            "Books / National Literature / Science Fiction",
            "Books / National Literature / Fiction Fantastic",
            "Books / Foreign Literature",
            "Books / Computers",
            "Books / Computers / Applications",
            "Books / Computers / Database",
            "Books / Computers / Programming",
            "Games",
            "Games / XBOX 360",
            "Games / XBOX 360 / Console",
            "Games / XBOX 360 / Games",
            "Games / XBOX 360 / Accessories",
            "Games / XBOX One",
            "Games / XBOX One / Console",
            "Games / XBOX One / Games",
            "Games / XBOX One / Accessories",
            "Games / Playstation 4",
        ]

    def test_import_categories(self):
        csv_file = create_tempcsv_file(self.categories)
        args = ['test_channel', csv_file]
        opts = {}

        try:
            call_command('importcategories', *args, **opts)
        finally:
            os.unlink(csv_file)

        channel = models.Channel.objects.filter(name=args[0])
        self.assertIsNotNone(channel)
        channel_categories = models.Category.objects.filter(channel=channel)
        self.assertEqual(channel_categories.count(), len(self.categories))

    def test_reimport_categories(self):
        csv_file = create_tempcsv_file(self.categories)
        args = ['test_channel', csv_file]
        opts = {}

        try:
            call_command('importcategories', *args, **opts)
        finally:
            os.unlink(csv_file)

        channel = models.Channel.objects.filter(name=args[0])
        self.assertIsNotNone(channel)
        channel_categories = models.Category.objects.filter(channel=channel)
        self.assertEqual(channel_categories.count(), len(self.categories))
