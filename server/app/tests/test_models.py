from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelCase(TestCase):
    """Test case user model"""

    def test_sample(self):
        """Test that 1 + 1 equals 2."""
        self.assertEqual(1 + 1, 2)
    
    def test_django_is_installed(self):
        """Test create user with email is successful"""
        email = 'test@example.com'
        password = 'testpass'
        user = get_user_model().objects.create_user(email=email, password=password) 

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_yet_another_test(self):
        pass