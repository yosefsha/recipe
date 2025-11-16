"""
Django commant to wait for db
"""
import time
from psycopg2 import OperationalError as  Psycopg2OpError
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

class Command(BaseCommand):
    """Django commant to wait for db"""
    def handle(self, *args, **options):
        self.stdout.write('waiting for db...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['defaults'])
                db_up = True
            except (OperationalError, Psycopg2OpError):
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('Database available!'))
        
