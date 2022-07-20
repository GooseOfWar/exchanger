from django.db import models


class ContactUs(models.Model):
    email_from = models.EmailField()
    email_to = models.EmailField()
    subject = models.CharField(max_length=254)
    message = models.CharField(max_length=10000)
