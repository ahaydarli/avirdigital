from django.contrib import admin
from linguist.admin import TranslatableModelAdmin
from .models import Page
# Register your models here.

class PageAdmin(TranslatableModelAdmin):
    list_display = ('title', 'created_at')

admin.site.register(Page, PageAdmin)