from django.urls import path

from . import views

urlpatterns = [
    path("registration/", views.RegisterUserView.as_view(), name="registration-page"),
    path("login/", views.LoginUserView.as_view(), name="login-page"),
    path("logout/", views.LogoutUserView.as_view(), name="logout-page"),
    path('profile/', views.UserProfileView.as_view(), name='profile-page'),
]
