from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def add_arguments(self, parser): 
        return super().add_arguments(parser)