# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Define a 'dashboard' URL pattern
    path('logout/', views.user_logout, name='logout'),
]
