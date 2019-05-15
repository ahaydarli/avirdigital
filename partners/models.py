from django.db import models
from portfolio.models import Portfolio
# Create your models here.

class Partner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(max_length=255, upload_to='partners')
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title

