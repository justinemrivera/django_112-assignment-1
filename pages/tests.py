from django.test import SimpleTestCase
from django.urls import reverse


class SimpleTests(SimpleTestCase):
    def test_home_page_status(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_about_page_status(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_about_page_contains_name(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Justine Rivera")

    def test_home_page_extends_base(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "base.html")

    def test_about_page_extends_base(self):
        response = self.client.get("/about/")
        self.assertTemplateUsed(response, "base.html")

    def test_home_page_uses_correct_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "base.html")

    def test_about_page_uses_correct_template(self):
        response = self.client.get("/about/")
        self.assertTemplateUsed(response, "about.html")

    def test_home_page_reverse_lookup(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_reverse_lookup(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_template_not_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateNotUsed(response, 'home.html')


# Create your tests here.
