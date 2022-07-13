"""Views"""
# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_foo(request):
    """First foo"""
    return HttpResponse("Gooses is our gods")
