from django.contrib import admin
from .models import *
from io import StringIO
from django.http import HttpResponse
import csv
# Register your models here.


class TmbreportAdmin(admin.ModelAdmin):
    list_display = ('dateReport',)
    actions = ['download_csv']

    def get_date_formatted(self, obj):
        if obj:
            return obj.date.date()
    get_date_formatted.admin_order_field = 'date'
    get_date_formatted.short_description = 'date'

    def download_csv(self, request, queryset):
        f = StringIO()
        writer = csv.writer(f)
        fieldsArray = [i.name for i in Tmbreport._meta.get_fields()][1:]
        writer.writerow(fieldsArray)

        for s in queryset:
            fieldsDataRow = [s.__dict__[i] for i in fieldsArray]
            writer.writerow(fieldsDataRow)

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Talamban_report.csv'
        return response


class LabreportAdmin(admin.ModelAdmin):
    list_display = ('dateReport',)
    actions = ['download_csv']

    def get_date_formatted(self, obj):
        if obj:
            return obj.date.date()
    get_date_formatted.admin_order_field = 'date'
    get_date_formatted.short_description = 'date'

    def download_csv(self, request, queryset):
        f = StringIO()
        writer = csv.writer(f)
        fieldsArray = [i.name for i in Labreport._meta.get_fields()][1:]
        writer.writerow(fieldsArray)

        for s in queryset:
            fieldsDataRow = [s.__dict__[i] for i in fieldsArray]
            writer.writerow(fieldsDataRow)

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Labangon_report.csv'
        return response


class KalimpreportAdmin(admin.ModelAdmin):
    list_display = ('dateReport',)
    actions = ['download_csv']

    def get_date_formatted(self, obj):
        if obj:
            return obj.date.date()
    get_date_formatted.admin_order_field = 'date'
    get_date_formatted.short_description = 'date'

    def download_csv(self, request, queryset):
        f = StringIO()
        writer = csv.writer(f)
        fieldsArray = [i.name for i in Kalimpreport._meta.get_fields()][1:]
        writer.writerow(fieldsArray)

        for s in queryset:
            fieldsDataRow = [s.__dict__[i] for i in fieldsArray]
            writer.writerow(fieldsDataRow)

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Kalimpyo_report.csv'
        return response


admin.site.register(Tmbreport, TmbreportAdmin)
admin.site.register(Labreport, LabreportAdmin)
admin.site.register(Kalimpreport, KalimpreportAdmin)
