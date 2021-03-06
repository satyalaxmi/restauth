from django.urls import path
from authapp.views.api_view import ProfileView, ProfileDetails, LogoutView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view()),
    path("profile/", ProfileView.as_view()),
    path("profile/<int:pk>", ProfileDetails.as_view()),
]