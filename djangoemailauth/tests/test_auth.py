from django.contrib.auth import authenticate
from django.test import TestCase

from djangoemailauth.models import EmailUser


class AuthenticateTest(TestCase):

    def setUp(self):
        self.user = EmailUser.objects.create_user(password="password", email="email@email.com", is_active=True)
        self.user.full_clean()

    def test_email_authenticate(self):
        user = authenticate(email="email@email.com", password="password")

        self.assertIsNotNone(user)
