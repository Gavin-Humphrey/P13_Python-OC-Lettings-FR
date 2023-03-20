from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Profile


class TestLetting(TestCase):
    def setUp(self):

        user_info = User.objects.create(
            username="FakeUser",
            first_name="Fake",
            last_name="User",
            email="usermail@user",
            password="abc1234",
        )
        Profile.objects.create(user=user_info, favorite_city="London")

    def test_lettings_index(self):
        response = self.client.get(reverse("profiles:index"))
        markup = response.content
        assert response.status_code == 200
        assert b"<title>Profiles</title>" in markup

    def test_user_info(self):
        response = self.client.get(reverse("profiles:profile", args={"FakeUser"}))
        markup = response.content
        assert response.status_code == 200
        assert b"<h1>FakeUser</h1>" in markup
