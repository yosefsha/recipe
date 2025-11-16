"""
Django commant to wait for db
"""

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django commant to wait for db"""
    def handle(self, *args, **options):
        return super().handle(*args, **options)