"""
URLS Header
"""
from django.urls import path

from exchanger import views

urlpatterns = [

    # contact us

    path('contact_us/', views.ContactUsCreateView.as_view(), name='contact_us'),

    # # source

    path('source/', views.SourceListView.as_view(), name='source_list'),
    path('source/create/', views.SourceCreateView.as_view(), name='source_create'),
    path('source/update/<int:pk>/', views.SourceUpdateView.as_view(), name='source_update'),
    path('source/delete/<int:pk>/', views.SourceDeleteView.as_view(), name='source_delete'),



    # rate

    path('rate/', views.RateListView.as_view(), name='rate_list'),
    path('rate/create/', views.RateCreateView.as_view(), name='rate_create'),
    path('rate/update/<int:pk>/', views.RateUpdateView.as_view(), name='rate_update', ),
    path('rate/delete/<int:pk>/', views.RateDeleteView.as_view(), name='rate_delete'),
    path('rate/details/<int:pk>/', views.RateDetailsView.as_view(), name='rate_details'),

    # log
    path('log/', views.ResponseLogView.as_view(), name='log_list'),

    # goose
    path('goose/', views.GooseView.as_view(), name='goose'),

]
