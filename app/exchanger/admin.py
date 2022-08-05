"""
More info: search django admin
"""

from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from exchanger.models import Rate, ContactUs, Source


class RateResource(resources.ModelResource):

    class Meta:
        model = Rate


class RateAdmin(ImportExportModelAdmin):
    list_display: tuple = (
        'base_currency_type',
        'currency_type',
        'sale',
        'buy',
        'source',
        'created',
    )
    list_filter = (
        'base_currency_type',
        'currency_type',
        'source',
    )
    list_per_page = 48

    resource_class = RateResource


class SourceAdmin(admin.ModelAdmin):
    list_display: tuple = (
        'source_url',
        'name',
        'created',
    )
    list_filter = (
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
    list_per_page = 48

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(Rate, RateAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
