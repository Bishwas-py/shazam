from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from authentication import views

# PARENT URL PATH: auth/
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('register/', views.RegisterView.as_view(), name='register'),
    path('user/', views.UserView.as_view(), name='get_user_by_token'),
    path('confirm-email/', views.ConfirmEmailView.as_view(), name='confirm_email'),
]
