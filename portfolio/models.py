from django.db import models
from six import with_metaclass
from django.utils.translation import ugettext_lazy as _

from linguist.metaclasses import ModelMeta as LinguistMeta
from linguist.mixins import ManagerMixin as LinguistManagerMixin
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from services.models import Service


class PortfolioManager(LinguistManagerMixin, models.Manager):
    pass

class PortfolioCategory(with_metaclass(LinguistMeta, models.Model)):
    title = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(PortfolioCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('portfolio category')
        verbose_name_plural = _('portfolio categories')
        linguist = {
            'identifier': 'portfolio category',
            'fields': ('title',),
            'default_language': 'az',
        }
class PortfolioImages(models.Model):
    file = models.ImageField(upload_to='portfolio')
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)

class Portfolio(with_metaclass(LinguistMeta, models.Model)):
    title = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    body = RichTextField(null=True)
    image = models.ImageField(upload_to='portfolio', max_length=255, null=True)
    image_back = models.ImageField(upload_to='portfolio', max_length=255, null=True)
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE)
    url = models.CharField(max_length=255, blank=True)
    customer = models.CharField(max_length=255, blank=True)
    date = models.DateField(blank=True, null=True)
    services = models.ManyToManyField(Service)
    created_at = models.DateTimeField(auto_now_add=True)
    position = models.IntegerField(blank=True)
    home = models.BooleanField(_('Display at home'), default=False)
    objects = PortfolioManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Portfolio, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('portfolio')
        verbose_name_plural = _('portfolios')
        linguist = {
            'identifier': 'portfolio',
            'fields': ('title', 'body'),
            'default_language': 'az',
        }



