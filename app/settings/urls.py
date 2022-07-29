"""URLS Header
"""
from django.contrib import admin
from django.urls import path

from exchanger.views import contact_us, rate_list, rate_create, rate_update, rate_delete, \
    index, rate_details, source_list, source_create, source_update, source_delete, goose

urlpatterns = [
    path('admin/', admin.site.urls),

    path('contact_us/', contact_us),
    path('rate/', rate_list),
    path('rate/create/', rate_create),
    path('rate/update/<int:rate_id>/', rate_update),
    path('rate/delete/<int:rate_id>/', rate_delete),
    path('rate/details/<int:rate_id>/', rate_details),

    path('source/', source_list),
    path('source/create/', source_create),
    path('source/update/<int:source_id>/', source_update),
    path('source/delete/<int:source_id>/', source_delete),

    path('goose/', goose),

    path('', index)
]
