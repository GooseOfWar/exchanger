"""
Views header
"""
from django.http import HttpResponse  #  pylint: disable=import-error
from django.shortcuts import render

from exchanger.models import ContactUs, Rate


def index(request):
    return render(request, 'exchanger/index.html')


def contact_us(request):  # pylint: disable=unused-argument
    """
    Function show data in ContactUs model
    """
    context = {
        'contact_us': ContactUs.objects.all()
    }
    return render(request, 'exchanger/contact_us.html', context=context)


def rate_list(request):
    context = {
        'rate_list': Rate.objects.all()
    }
    return render(request, 'exchanger/rate_list.html', context=context)
