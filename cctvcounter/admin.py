from django.contrib import admin
from .models import *
from io import StringIO
import csv
from django.http import HttpResponse

# Register your models here.


class TmbcamcountAdmin(admin.ModelAdmin):
    list_display = ('date',)
    actions = ['download_csv']

    def get_date_formatted(self, obj):
        if obj:
            return obj.date.date()
    get_date_formatted.admin_order_field = 'date'
    get_date_formatted.short_description = 'date'

    def download_csv(self, request, queryset):
        f = StringIO()
        writer = csv.writer(f)
        fieldsArray = [i.name for i in Tmbcamcount._meta.get_fields()][1:]
        writer.writerow(fieldsArray)

        for s in queryset:
            fieldsDataRow = [s.__dict__[i] for i in fieldsArray]
            writer.writerow(fieldsDataRow)

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Talamban_cctv.csv'
        return response


class TmbcamcountAdmin(admin.ModelAdmin):
    list_display = ('date',)
    actions = ['download_csv']

    def get_date_formatted(self, obj):
        if obj:
            return obj.date.date()
    get_date_formatted.admin_order_field = 'date'
    get_date_formatted.short_description = 'date'

    def download_csv(self, request, queryset):
        f = StringIO()
        writer = csv.writer(f)
        fieldsArray = [i.name for i in Tmbcamcount._meta.get_fields()][1:]
        writer.writerow(fieldsArray)

        for s in queryset:
            fieldsDataRow = [s.__dict__[i] for i in fieldsArray]
            writer.writerow(fieldsDataRow)

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Talamban_cctv.csv'
        return response


class LabcamcountAdmin(admin.ModelAdmin):
    list_display = ('date',)
    actions = ['download_csv']

    def get_date_formatted(self, obj):
        if obj:
            return obj.date.date()
    get_date_formatted.admin_order_field = 'date'
    get_date_formatted.short_description = 'date'

    def download_csv(self, request, queryset):
        f = StringIO()
        writer = csv.writer(f)
        fieldsArray = [i.name for i in Labcamcount._meta.get_fields()][1:]
        writer.writerow(fieldsArray)

        for s in queryset:
            fieldsDataRow = [s.__dict__[i] for i in fieldsArray]
            writer.writerow(fieldsDataRow)

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Talamban_cctv.csv'
        return response


class KalcamcountAdmin(admin.ModelAdmin):
    list_display = ('date',)
    actions = ['download_csv']

    def get_date_formatted(self, obj):
        if obj:
            return obj.date.date()
    get_date_formatted.admin_order_field = 'date'
    get_date_formatted.short_description = 'date'

    def download_csv(self, request, queryset):
        f = StringIO()
        writer = csv.writer(f)
        fieldsArray = [i.name for i in Kalcamcount._meta.get_fields()][1:]
        writer.writerow(fieldsArray)

        for s in queryset:
            fieldsDataRow = [s.__dict__[i] for i in fieldsArray]
            writer.writerow(fieldsDataRow)

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Talamban_cctv.csv'
        return response


class GoldswancamcountAdmin(admin.ModelAdmin):
    list_display = ('date',)
    actions = ['download_csv']

    def get_date_formatted(self, obj):
        if obj:
            return obj.date.date()
    get_date_formatted.admin_order_field = 'date'
    get_date_formatted.short_description = 'date'

    def download_csv(self, request, queryset):
        f = StringIO()
        writer = csv.writer(f)
        fieldsArray = [i.name for i in Goldswancamcount._meta.get_fields()][1:]
        writer.writerow(fieldsArray)

        for s in queryset:
            fieldsDataRow = [s.__dict__[i] for i in fieldsArray]
            writer.writerow(fieldsDataRow)

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Talamban_cctv.csv'
        return response


admin.site.register(Tmbcamcount, TmbcamcountAdmin)
admin.site.register(Labcamcount, LabcamcountAdmin)
admin.site.register(Kalcamcount, KalcamcountAdmin)
admin.site.register(Goldswancamcount, GoldswancamcountAdmin)
