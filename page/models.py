from django.db import models
from django.template.defaultfilters import slugify
from django.utils.six import with_metaclass
from django.utils.translation import ugettext_lazy as _
from uuid import uuid4
from linguist.metaclasses import ModelMeta as LinguistMeta
from linguist.mixins import ManagerMixin as LinguistManagerMixin
from ckeditor.fields import RichTextField

# Create your models here.

class Page(with_metaclass(LinguistMeta, models.Model)):
    title = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    text = RichTextField(null=True)
    # image = FilerImageField(null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')
        linguist = {
            'identifier': 'page',
            'fields': ('title', 'text'),
            'default_language': 'az',
        }
