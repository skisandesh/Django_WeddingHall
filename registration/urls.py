from django.urls import path, include
from .import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import auth_login, auth_logout
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_login, {'template_name': 'registration/login.html'}, name='login'),
    path('logout/',auth_logout,name='logout'),

]