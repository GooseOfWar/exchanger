"""
Views header
Class View model get from ccbv.co.uk
"""
from django.urls import reverse_lazy
from django.views import generic

from exchanger.forms import RateForm, SourceForm, ContactUsForm
from exchanger.models import ContactUs, Rate, Source, ResponseLog


class IndexView(generic.TemplateView):
    template_name = 'exchanger/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rate_count'] = Rate.objects.count()
        return context

# Contact Us
# zochem?
class ContactUsView(generic.ListView):
    queryset = ContactUs.objects.all()
    template_name = 'exchanger/contact_us.html'


class ContactUsCreateView(generic.CreateView):
    queryset = ContactUs.objects.all()
    template_name = 'exchanger/contact_us_create.html'
    form_class = ContactUsForm
    success_url = '/'


# RATE
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


class RateDetailsView(generic.DeleteView):
    queryset = Rate.objects.all()
    template_name = 'exchanger/rate_details.html'


# SOURCE
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


# LOG
class ResponseLogView(generic.ListView):
    queryset = ResponseLog.objects.all()
    template_name = 'exchanger/log_list.html'



# GOOSE
class GooseView(generic.TemplateView):
    template_name = 'exchanger/goose.html'
