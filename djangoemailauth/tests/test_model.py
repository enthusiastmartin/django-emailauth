"""Tests for the models of the djangoemailauth app."""
from django.test import TestCase

from djangoemailauth.models import AbstractEmailUser


# from mixer.backend.django import mixer

class TestUser(AbstractEmailUser):
    pass


class UserModelTest(TestCase):

    def test_string_representation(self):
        pass
