from django.test import TestCase
from django.urls import reverse


class TestHomepage(TestCase):

    def test_hompage_index(self):
        response = self.client.get(reverse("homepage:index"))
        markup = response.content
        assert response.status_code == 200
        assert b"<title>Holiday Homes</title>" in markup
