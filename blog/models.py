from django.db import models
from django.template.defaultfilters import slugify
from django.utils.six import with_metaclass
from django.utils.translation import ugettext_lazy as _
from uuid import uuid4
from linguist.metaclasses import ModelMeta as LinguistMeta
from linguist.mixins import ManagerMixin as LinguistManagerMixin
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class BlogManager(LinguistManagerMixin, models.Manager):
    pass


class BlogCategory(with_metaclass(LinguistMeta, models.Model)):
    title = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('blog category')
        verbose_name_plural = _('blog categories')
        linguist = {
            'identifier': 'blog category',
            'fields': ('title',),
            'default_language': 'az',
        }


class Blog(with_metaclass(LinguistMeta, models.Model)):
    title = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=True)
    text = RichTextField(null=True)
    image = models.ImageField(max_length=255, upload_to='blog', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)


    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')
        linguist = {
            'identifier': 'blog',
            'fields': ('title', 'text'),
            'default_language': 'az',
        }
