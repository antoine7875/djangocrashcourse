from django.urls import path

from .views import welcome, login, register, modify_profile, logout, option1

app_name = 'todos'

urlpatterns = [
    path('', welcome),
    path('welcome', welcome),
    path('login', login),
    path('logout', logout),
    path('register', register),
    path('modify_profile', modify_profile),
    path('option1', option1),
]