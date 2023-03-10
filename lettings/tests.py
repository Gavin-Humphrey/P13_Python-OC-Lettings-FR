from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


class TestLetting(TestCase):

    def setUp(self):
        address = Address.objects.create(
            number = 1,
            street = "High Park",
            city = "LA",
            state = "CA",
            zip_code = 500086,
            country_iso_code = "USA"
        )
        self.letting = Letting.objects.create(title="Fake Letting", address=address)



    def test_lettings_index(self):
        response = self.client.get(reverse("lettings:index"))
        markup = response.content
        assert response.status_code == 200
        assert b"<title>Lettings</title>" in markup

    
    def test_lettings_info(self):
        response = self.client.get(reverse("lettings:letting", kwargs={"letting_id":self.letting.id}))
        markup = response.content
        assert response.status_code == 200
        assert b"<title>Fake Letting</title>" in markup

   