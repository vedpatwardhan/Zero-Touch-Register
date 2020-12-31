from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import visitor
# admin.site.register(visitor)
@admin.register(visitor)
class ViewAdmin(ImportExportModelAdmin):
    pass