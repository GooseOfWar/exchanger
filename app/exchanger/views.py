"""
Views header
"""
# from django.shortcuts import render
from django.http import HttpResponse  #  pylint: disable=import-error
from exchanger.models import ContactUs


def contact_us(request):  # pylint: disable=unused-argument
    """
    Function show data in ContactUs model
    """
    contact_us_list: list = []
    for contact_case in ContactUs.objects.all():
        html_str: str = f'\
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2//EN">\
        <p> MESSAGE ID: {contact_case.id}</p>\
        <p style="margin-left: 30px;">FROM: {contact_case.email_from}</p>\
        <p style="margin-left: 30px;">TO: {contact_case.email_to}</p>\
        <p style="margin-left: 30px;">SUBJECT: {contact_case.subject}</p>\
        <p style="margin-left: 50px;">{contact_case.message}</p>'
        contact_us_list.append(html_str)
        result: str = str(contact_us_list).replace("', '", '')
    return HttpResponse(result)  # noqa
