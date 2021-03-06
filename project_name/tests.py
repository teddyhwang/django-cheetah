from django.core.urlresolvers import reverse
from django.test import TestCase


class HomePageTest(TestCase):
    def test_home_page_renders(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class AboutPageTest(TestCase):
    def test_about_page_renders(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
