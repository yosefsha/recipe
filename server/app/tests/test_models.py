from django.test import TestCase
import django

class SampleTestCase(TestCase):
    """Sample test case."""

    def test_sample(self):
        """Test that 1 + 1 equals 2."""
        self.assertEqual(1 + 1, 2)
    
    def test_django_is_installed(self):
        """Test Django is properly installed."""
        self.assertTrue(hasattr(django, 'VERSION'))
    
    def test_yet_another_test(self):
        pass