"""URLS Header
"""
from django.contrib import admin
from django.urls import path

from exchanger.views import contact_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact_us/', contact_us)
]
