"""
Models header
"""
from django.db import models
from exchanger.model_choices import CURRENCY_TYPES


class ContactUs(models.Model):
    email_from = models.EmailField()
    email_to = models.EmailField(default='ma@mail.com')
    subject = models.CharField(max_length=254)
    message = models.CharField(max_length=10000)
    received = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Users Mail'
        verbose_name_plural = 'Users Mails'
        ordering = ['received', 'id']


class Rate(models.Model):
    base_currency_type = models.CharField(max_length=3, choices=CURRENCY_TYPES)
    currency_type = models.CharField(max_length=3, choices=CURRENCY_TYPES)
    sale = models.DecimalField(max_digits=16, decimal_places=4)
    buy = models.DecimalField(max_digits=16, decimal_places=4)
    source = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Rate List'
        verbose_name_plural = 'Rate List'
        ordering = ['created', 'id']

    def __str__(self):
        return self.name


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Source List'
        verbose_name_plural = 'Source List'
        ordering = ['created', 'id']


class ResponseLog(models.Model):
    response_time = models.DecimalField(max_digits=7, decimal_places=5)
    request_method = models.CharField(max_length=10)
    query_params = models.CharField(max_length=256)
    ip = models.CharField(max_length=15)
    path = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
