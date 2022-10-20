
from django.urls import path, include

urlpatterns = [
    path('', include('api.urls')),
    path('auth/', include('rest_framework.urls')),
]
