"""Tests for the models of the djangoemailauth app."""
from django.test import TestCase

# from mixer.backend.django import mixer
from djangoemailauth.models import EmailUser


class UserModelTest(TestCase):

    def setUp(self):
        self.user = EmailUser.objects.create_user(password="password", email="email@email.com")
        self.user.full_clean()

    def test_string_representation(self):
        self.assertEqual(str(self.user), "email@email.com")
