"""URLS Header
"""
from django.contrib import admin
from django.urls import path

from exchanger.views import contact_us, rate_list, index

urlpatterns = [
    path('admin/', admin.site.urls),

    path('contact_us/', contact_us),
    path('rate/', rate_list),
    path('', index)
]
