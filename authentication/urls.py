from django.urls import path

from . import views

urlpatterns = [
    path('registration/', views.register_user, name='registration-view'),
    path('login/', views.user_login, name='login-view'),
    path('logout/', views.user_logout, name='logout-view'),
]