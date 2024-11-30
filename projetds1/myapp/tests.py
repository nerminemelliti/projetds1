from django.test import TestCase
from django.urls import reverse

class SimpleTest(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello, CI/CD!"})

# Create your tests here.
