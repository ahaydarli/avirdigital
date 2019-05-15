from django.db import models
from django.utils.six import with_metaclass
from django.utils.translation import ugettext_lazy as _
from uuid import uuid4
from linguist.metaclasses import ModelMeta as LinguistMeta
from linguist.mixins import ManagerMixin as LinguistManagerMixin

# Create your models here.

class About(with_metaclass(LinguistMeta, models.Model)):
    title = models.CharField(max_length=255, null=True)
    text = models.TextField(null=True)
    icon = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('about item')
        verbose_name_plural = _('about items')
        linguist = {
            'identifier': 'about item',
            'fields': ('title', 'text'),
            'default_language': 'az',
        }
