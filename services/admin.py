from django.contrib import admin
from linguist.admin import TranslatableModelAdmin
from .models import Service, SubService
from django.utils.safestring import mark_safe
# Register your models here.

class ServiceAdmin(TranslatableModelAdmin):
    list_display = ('title', 'created_at', 'position')

class SubServiceAdmin(TranslatableModelAdmin):
    list_display = ('title', 'created_at')


admin.site.register(Service, ServiceAdmin)
admin.site.register(SubService, SubServiceAdmin)

