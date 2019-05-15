from django.contrib import admin
from linguist.admin import TranslatableModelAdmin
from .models import About
# Register your models here.

class AboutAdmin(TranslatableModelAdmin):
    list_display = ('title', 'created_at')

admin.site.register(About, AboutAdmin)