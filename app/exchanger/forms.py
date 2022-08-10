"""
Documentation look at: django form initial
"""

from django import forms

from exchanger.models import Rate, Source, ContactUs


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'base_currency_type',
            'currency_type',
            'sale',
            'buy',
            'source'
        )


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            'source_url',
            'name'
        )


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'email_from',
            'subject',
            'message'
        )
