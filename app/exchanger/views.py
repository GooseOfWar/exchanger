"""
Views header
"""
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse

from django.views import generic

from exchanger.models import ContactUs, Rate, Source
from exchanger.forms import RateForm, SourceForm


class IndexView (generic.TemplateView):
    template_name = 'exchanger/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rate_count'] = Rate.objects.count()
        return context


class ContactUsView(generic.ListView):
    queryset = ContactUs.objects.all()
    template_name = 'exchanger/contact_us.html'


class RateListView(generic.ListView):
    queryset = Rate.objects.all()
    template_name = 'exchanger/rate_list.html'


class RateCreateView(generic.CreateView):
    queryset = Rate.objects.all()
    template_name = 'exchanger/rate_create.html'
    form_class = RateForm
    success_url = reverse_lazy('rate_list')


class RateUpdateView(generic.UpdateView):
    queryset = Rate.objects.all()
    template_name = 'exchanger/rate_update.html'
    form_class = RateForm
    success_url = reverse_lazy('rate_list')


class RateDeleteView(generic.DeleteView):
    queryset = Rate.objects.all()
    template_name = 'exchanger/rate_delete.html'
    success_url = reverse_lazy('rate_list')


class RateDetails(generic.DeleteView):
    queryset = Rate.objects.all()
    template_name = 'exchanger/rate_details.html'

class SourceListView(generic.ListView):
    """
    Page with source list
    """
    queryset = Source.objects.all()
    template_name = 'exchanger/source_list.html'



class SourceCreateView(generic.CreateView):
    queryset = Source.objects.all()
    template_name = 'exchanger/source_create.html'
    form_class = SourceForm
    success_url = reverse_lazy('source_list')


class SourceUpdateView(generic.UpdateView):
    queryset = Source.objects.all()
    template_name = 'exchanger/source_update.html'
    form_class = SourceForm
    success_url = reverse_lazy('source_list')


class SourceDeleteView(generic.DeleteView):
    queryset = Source.objects.all()
    template_name = 'exchanger/source_delete.html'
    success_url = reverse_lazy('source_list')


class GooseView(generic.TemplateView):
    template_name = 'exchanger/goose.html'


