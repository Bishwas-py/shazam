from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from authentication.models import Profile, Status


class TestUserView(APITestCase):
    def test_register_user(self):
        url = reverse('register')
        response = self.client.post(url, {
            'username': 'testuser',
            'email': 'testuser@gmail.com',
            'password': 'test_password',
            'password_confirmation': 'test_password',
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        self.test_register_user()

        url = reverse('token_obtain_pair')
        response = self.client.post(url, {
            'username': 'testuser',
            'password': 'test_password',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        return response.data['access'], response.data['refresh']

    def test_get_user_by_token(self):
        access, refresh = self.test_login_user()

        url = reverse('get_user_by_token')
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {access}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(Status.objects.count(), 1)

    def test_confirm_email_with_wrong_token(self):
        self.test_login_user()
        access = "Wrong token"

        url = reverse('confirm_email')
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {access}')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        user = User.objects.get()
        self.assertEqual(user.status.is_confirmed, False)

    def test_confirm_email(self):
        access, refresh = self.test_login_user()

        url = reverse('confirm_email')
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {access}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user = User.objects.get()
        self.assertEqual(user.status.is_confirmed, False)

        token = user.status.token_key
        response = self.client.post(url, {'token': token}, HTTP_AUTHORIZATION=f'Bearer {access}')

        user = User.objects.get()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(user.status.is_confirmed, True)
        self.assertEqual(user.status.token_key, None)


def test_get_user(self):
    self.test_register_user()
    url = reverse('get_user_by_token')
