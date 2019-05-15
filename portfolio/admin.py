
# Register your models here.
from django.contrib import admin
from linguist.admin import TranslatableModelAdmin
from .models import Portfolio, PortfolioCategory, PortfolioImages
from django.utils.safestring import mark_safe

class PortfolioFileInline(admin.TabularInline):
    model = PortfolioImages

class PortfolioAdmin(TranslatableModelAdmin):
    list_display = ('title', 'created_at', 'position')
    # readonly_fields = ["main_image"]
    inlines = [PortfolioFileInline, ]
    # def main_image(self, obj):
    #     return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
    #         url=obj.image.url,
    #         width='300px',
    #         height='100%'
    #     )
    #     )

class PortfolioCategoryAdmin(TranslatableModelAdmin):
    list_display = ('title', 'created_at')

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioCategory, PortfolioCategoryAdmin)