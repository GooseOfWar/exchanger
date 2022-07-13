"""Views"""
# from django.shortcuts import render
from django.http import HttpResponse  #  pylint: disable=import-error

# Create your views here.
def first_foo(request):  # pylint: disable=unused-argument
    """First foo"""
    return HttpResponse("Gooses is our gods")
