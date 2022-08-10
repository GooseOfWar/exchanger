"""
More info: search django admin
"""

from django.contrib import admin

from import_export import resources
from import_export.admin import ExportMixin

from exchanger.models import Rate, ContactUs, Source, ResponseLog


class RateResource(resources.ModelResource):

    class Meta:
        model = Rate


class RateAdmin(ExportMixin, admin.ModelAdmin):
    list_display: tuple = (
        'base_currency_type',
        'currency_type',
        'sale',
        'buy',
        'source',
        'created',
    )
    list_filter: tuple = (
        'base_currency_type',
        'currency_type',
        'source',
    )
    list_per_page: int = 48

    resource_class = RateResource

    def get_export_formats(self):
        fmt: list = super().get_export_formats()
        allowed_fmt: list[str] = ['CSV', 'XLSX']
        formats: list = [i for i in fmt if i.__name__ in allowed_fmt]
        return formats




class SourceAdmin(admin.ModelAdmin):
    list_display: tuple = (
        'source_url',
        'name',
        'created',
    )
    list_filter: tuple = (
        'source_url',
        'name',
    )
    list_per_page = 48


class ContactUsAdmin(admin.ModelAdmin):
    list_display: tuple = (
        'subject',
        'email_from',
        'email_to',
        'received'
    )
    list_per_page: int = 48

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


# Log

class LogAdmin(admin.ModelAdmin):
    list_display: tuple = (
        'response_time',
        'request_method',
        'query_params',
        'ip',
        'path',
        'created',
    )
    list_filter: tuple = (
        'request_method',
        'path',
    )
    list_per_page = 48


admin.site.register(Rate, RateAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(ResponseLog, LogAdmin)
