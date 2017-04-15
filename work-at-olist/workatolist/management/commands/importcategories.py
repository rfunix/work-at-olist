from django.core.management.base import BaseCommand, CommandError
from workatolist.models import Channel, Category


class Command(BaseCommand):
    help = "The Command received channel and csv to import categories"

    def add_arguments(self, parser):
        parser.add_argument("channel", nargs="+", type=str)
        parser.add_argument("csv_file", nargs="+", type=str)

    def handle(self, *args, **options):
        channel = options["channel"][0]
        csv_file = options["csv_file"][0]
        self.create_channel(channel)

    def create_channel(self, channel):
        obj, created = Channel.objects.update_or_create(
            name=channel
        )
