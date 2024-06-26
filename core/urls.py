from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.user_registration, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
]