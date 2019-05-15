from django.contrib import admin
from linguist.admin import TranslatableModelAdmin
from .models import Blog, BlogCategory
# Register your models here.

class BlogCategoryAdmin(TranslatableModelAdmin):
    list_display = ('title', 'created_at')

class BlogAdmin(TranslatableModelAdmin):
    list_display = ('title', 'created_at')

admin.site.register(BlogCategory, BlogCategoryAdmin)

admin.site.register(Blog, BlogAdmin)
