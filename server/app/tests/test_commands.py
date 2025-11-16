"""
Test custom Django anagement commands
"""

from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.test import SimpleTestCase

class CommandTests(SimpleTestCase):
    """Test commands"""

    def test_wait_for_db_ready(self):
        """Test waiting for db to be ready"""
