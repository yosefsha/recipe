"""
Test custom Django anagement commands
"""

from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(TestCase):
    """Test commands"""
    def test_wait_for_db_ready(self, patched_check):
        patched_check.return_value = True
        """Test waiting for db to be ready"""
        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])
    
    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test errors catched whed db init delayed """
        patched_check.side_effect = [Psycopg2Error] * 3 + \
        [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 7) # 3 errors each and then true

        patched_check.assert_called_with(databases=['default'])


