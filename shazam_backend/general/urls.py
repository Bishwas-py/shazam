from django.urls import path

from general import views

urlpatterns = [
    path('', views.Site.as_view(), name='site_info'),
]
