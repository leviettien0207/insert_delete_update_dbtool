from django.core.management.base import BaseCommand, CommandError
from apps.import_diamond import Import


class Command(BaseCommand):
    help = 'To progress dbtool'

    def add_arguments(self, parser):
        parser.add_argument('-f', '-filepath')

    def handle(self, *args, **options):
        fh = options['f']
        handle = Import()
        handle.post(None, fh)
