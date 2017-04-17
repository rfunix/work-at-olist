from django.core.management.base import BaseCommand, CommandError
from api.models import Channel, Category
import csv


class Command(BaseCommand):
    help = "This Command received channel and csv to import categories"

    def add_arguments(self, parser):
        parser.add_argument("channel", nargs="+", type=str)
        parser.add_argument("csv_file", nargs="+", type=str)

    def handle(self, *args, **options):
        channel = self.create_channel(options["channel"][0])
        self.create_categories(options["csv_file"][0], channel)

    def create_channel(self, channel):
        obj, created = Channel.objects.update_or_create(
            name=channel
        )
        return obj

    def create_categories(self, csv_file, channel):
        for categories in self.parser_csv_file(csv_file):
            parent_category = None
            for category in categories:
                category = category.strip()
                parent_category = self.create_category(
                    category, parent_category, channel
                )

    def parser_csv_file(self, csv_file):
        with open(csv_file, newline='') as csv_data:
            reader = csv.reader(csv_data, delimiter="/")
            next(csv_data)
            for row in reader:
                yield row

    def create_category(self, category, parent_category, channel):
        print(category, parent_category)
        obj, created = Category.objects.update_or_create(
            name=category,
            parent=parent_category,
            channel=channel
        )
        return obj
