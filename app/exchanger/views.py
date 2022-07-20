"""Views"""
# from django.shortcuts import render
from django.http import HttpResponse  #  pylint: disable=import-error
from exchanger.models import ContactUs


def contact_us(request):  # pylint: disable=unused-argument
    contact_us_list: list = []
    for contact_case in ContactUs.objects.all():
        html_str: str = f'<p>ID: {contact_case.id} FROM: {contact_case.email_from}    TO: {contact_case.email_to}</p>'
        contact_us_list.append(html_str)
        result: str = str(contact_us_list).replace("', '", '')
    return HttpResponse(result)  # noqa
