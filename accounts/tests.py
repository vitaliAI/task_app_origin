from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
from accounts.forms import RegistrationForm, LoginForm
# Create your tests here.

class AccountsTest(TestCase):

    def setUp(self):
        self.register_data = {
            'email': 'test@example.com',
            'username': 'test_user',
            'password': 'test',
            'password_confirmation': 'test'
        }

        User.objects.create_user('test', 'test@example.com', 'test')


    def tearDown(self):
        User.objects.get(username='test').delete()

    def test_get_register_form(self):
        response = self.client.get(reverse('accounts:accounts_register'))
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertIsInstance(response.context['form'], RegistrationForm)

    def test_get_login_form(self):
        response = self.client.get(reverse('accounts:accounts_login'))
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.assertIsInstance(response.context['form'], LoginForm)

    def test_register(self):
        response = self.client.post(
            reverse('accounts:accounts_register'),
            data=self.register_data
        )
        # TODO Later
        self.assertRedirects(response, reverse('accounts:accounts_login'))
        # New user has been cerated
        self.assertIsNotNone(User.objects.get(username='test_user'))

    def test_login(self):
        # No user is logged in
        self.assertFalse('_auth_user_id' in self.client.session)
        login_data = {'username': 'test', 'password': 'test'}
        response = self.client.post(reverse('accounts:accounts_login'),
                                    data=login_data)
        # TODO
        self.assertRedirects(response, reverse('accounts:accounts_login'))
        # User is logged in
        self.assertEqual(self.client.session['_auth_user_id'], '1')

    def test_login_with_non_existent_user(self):
        login_data = {'username': 'test4', 'password': 'test'}
        response = self.client.post(reverse('accounts:accounts_login'),
                                    data=login_data)
        self.assertFalse('_auth_user_id' in self.client.session)
        self.assertRedirects(response, reverse('accounts:accounts_login'))

    def test_login_with_wrong_passord(self):
        login_data = {'username': 'test', 'password': 'test12'}
        response = self.client.post(reverse('accounts:accounts_login'),
                                    data=login_data)
        self.assertFalse('_auth_user_id' in self.client.session)
        # TODO test validation form
        self.assertRedirects(response, reverse('accounts:accounts_login'))
        error_message = 'Incorrect username and/or password.'
        self.assertContains(response, error_message, status_code=200)













