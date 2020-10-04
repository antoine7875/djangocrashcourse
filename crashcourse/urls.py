from django.contrib import admin
from django.urls import path, include

app_name = 'ant1'

urlpatterns = [
    path('',include('ant1.urls', namespace='ant1')),
    path('admin/', admin.site.urls),
]
