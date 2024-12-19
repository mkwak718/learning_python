from django.contrib import admin

# Register your models here.
from .models import PythonModule

class PythonModuleAdmin(admin.ModelAdmin):
    list_display = ('title', "published", "display_order",)

admin.site.register(PythonModule, PythonModuleAdmin)