from re import template
from django import views
from django.urls import path
from .views import UserEditForm, UserRegisterView, PasswordChangeView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('edit_profile/', UserEditForm.as_view(), name = 'edit_profile'),
    path('password/', PasswordChangeView.as_view(template_name = 'registration/change_password.html'), name = 'password'),
    path('password_success/', views.password_success, name = 'password_success'),
    
]
