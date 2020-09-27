from django.urls import path

from .views import welcome, login, register

app_name = 'todos'

urlpatterns = [
    path('', welcome),
    path('welcome', welcome),
    path('login', login),
    path('register', register)
]