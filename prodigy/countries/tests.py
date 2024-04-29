from django.test import TestCase, Client
from django.urls import reverse
from .models import Countries
import datetime
from urllib.parse import urlencode

class CountriesTestCase(TestCase):
  def setUp(self):
    self.client = Client()
    print("Setting up test data: create country.")
    self.country = Countries.objects.create(
      title="Test Country", 
      alpha2="TC", 
      alpha3="TCT", 
      is_deleted=False,
      created_at=datetime.datetime.now(),
      updated_at=datetime.datetime.now()
    )
    

  def test_get_countries(self):
    query_params = urlencode({
      'alpha2': self.country.alpha2,
      #'alpha3': self.country.alpha3
    })
    url = f"{reverse('countries-list')}?{query_params}"
    
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data[0]['title'], self.country.title)

  def test_delete_country(self):
    url = f"{reverse('countries-detail',kwargs={'pk': self.country.pk})}"
    response = self.client.delete(url)
    self.assertEqual(response.status_code, 204)

    url = f"{reverse('countries-undelete',kwargs={'pk': self.country.pk})}"
    response = self.client.put(url)
    self.assertEqual(response.status_code, 200)