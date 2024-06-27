from django.test import TestCase
from .forms import LoginForm
from django.urls import reverse
from django.contrib.auth.models import User


class LoginTestCase(TestCase):
    def setUp(self):
        self.username = 'newuser'
        self.password = 'password123'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_form(self):
        form = LoginForm(data={'username': self.username, 'password': self.password})
        self.assertTrue(form.is_valid())

    def test_successful_login(self):
        response = self.client.post(reverse('core:login'), {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('core:home'))

    def test_invalid_login(self):
        response = self.client.post(reverse('core:login'), {'username': self.username, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username or password. Please try again later.')



