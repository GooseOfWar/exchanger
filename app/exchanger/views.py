"""
Views header
"""
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404

from exchanger.models import ContactUs, Rate, Source
from exchanger.forms import RateForm, SourceForm


def index(request):
    """
    First page
    """
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
    """
    Page with rate list
    """
    context = {
        'rate_list': Rate.objects.all()
    }
    return render(request, 'exchanger/rate_list.html', context=context)


def rate_create(request):
    """CREATE NEW RAW"""
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/')
    elif request.method == 'GET':
        form = RateForm()
    context = {'form': form}
    return render(request, 'exchanger/rate_create.html', context=context)


def rate_update(request, rate_id):
    """UPDATE RAW"""

    rate_instance = get_object_or_404(Rate, id=rate_id)

    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate_instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/')
    elif request.method == 'GET':
        form = RateForm(instance=rate_instance)
    context = {'form': form}
    return render(request, 'exchanger/rate_update.html', context=context)


def rate_delete(request, rate_id):
    """DELETE RAW"""
    rate_instance = get_object_or_404(Rate, id=rate_id)

    if request.method == 'POST':
        rate_instance.delete()
        return HttpResponseRedirect('/rate/')

    context = {'instance': rate_instance}
    return render(request, 'exchanger/rate_delete.html', context=context)


def rate_details(request, rate_id):
    """SEE DETAILS"""
    rate_instance = get_object_or_404(Rate, id=rate_id)
    context = {'instance': rate_instance}
    return render(request, 'exchanger/rate_details.html', context=context)


def source_list(request):
    """
        Page with source list
    """
    context = {
        'source_list': Source.objects.all()
    }
    return render(request, 'exchanger/source_list.html', context=context)


def source_create(request):
    """CREATE NEW RAW"""
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/')
    elif request.method == 'GET':
        form = SourceForm()
    context = {'form': form}
    return render(request, 'exchanger/source_create.html', context=context)


def source_update(request, source_id):
    """UPDATE RAW"""

    source_instance = get_object_or_404(Source, id=source_id)

    if request.method == 'POST':
        form = SourceForm(request.POST, instance=source_instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/')
    elif request.method == 'GET':
        form = SourceForm(instance=source_instance)
    context = {'form': form}
    return render(request, 'exchanger/source_update.html', context=context)


def source_delete(request, source_id):
    """DELETE RAW"""
    source_instance = get_object_or_404(Source, id=source_id)

    if request.method == 'POST':
        source_instance.delete()
        return HttpResponseRedirect('/source/')

    context = {'instance': source_instance}
    return render(request, 'exchanger/source_delete.html', context=context)


def goose(request):
    """
    GOOSE page
    """
    return render(request, 'exchanger/goose.html')
