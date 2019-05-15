from django.db import models
from django.template.defaultfilters import slugify
from django.utils.six import with_metaclass
from django.utils.translation import ugettext_lazy as _
from uuid import uuid4
from linguist.metaclasses import ModelMeta as LinguistMeta
from linguist.mixins import ManagerMixin as LinguistManagerMixin
from ckeditor.fields import RichTextField

# Create your models here.
class ServiceManager(LinguistManagerMixin, models.Manager):
    pass

class SubService(with_metaclass(LinguistMeta, models.Model)):
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    icon = models.CharField(max_length=255, default='Null')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('sub service')
        verbose_name_plural = _('sub services')
        linguist = {
            'identifier': 'sub service',
            'fields': ('title', 'description'),
            'default_language': 'az',
        }

class Service(with_metaclass(LinguistMeta, models.Model)):
    title = models.CharField(max_length=255, null=True)
    slug = models.SlugField(unique=True, blank=True)
    sub_title = models.TextField(blank=True, null=True)
    short_description = models.TextField(null=True)
    description = RichTextField(null=True)
    image = models.ImageField(upload_to='service')
    image_description = models.CharField(max_length=255)
    sub_service = models.ManyToManyField(SubService, blank=True)
    icon = models.CharField(max_length=255, null=True)
    position = models.IntegerField(blank=True, default=0)
    home = models.BooleanField(_('Display at home'), default=False)
    created_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')
        linguist = {
            'identifier': 'service',
            'fields': ('title', 'sub_title', 'short_description', 'description'),
            'default_language': 'az',
        }




