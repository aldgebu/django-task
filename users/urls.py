from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView,
    CustomTokenObtainPairView,
    ChangePasswordView,
    UpdateProfileView
)

urlpatterns = [
    # Authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Profile management
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('update-profile/', UpdateProfileView.as_view(), name='update_profile'),
] 