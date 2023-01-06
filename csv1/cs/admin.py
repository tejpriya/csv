from django.contrib import admin
ImportError
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from cs.models import cv

@admin.register(cv)
class cvAdmin(ImportExportModelAdmin):

    list_display = ('name', 'address')
    class Meta:
        model=cv