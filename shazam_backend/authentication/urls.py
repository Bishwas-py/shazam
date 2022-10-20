from django.urls import path
from rest_framework.authtoken import views as authviews

from authentication import views

urlpatterns = [
    path('token-auth', authviews.obtain_auth_token, name='token-auth'),
    path('verify', views.verify_token, name='verify-token'),
]
