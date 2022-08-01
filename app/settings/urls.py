"""
URLS Header
"""
from django.contrib import admin
from django.urls import path, include

from exchanger import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.IndexView.as_view()),

    path('', include('exchanger.urls'))
]
