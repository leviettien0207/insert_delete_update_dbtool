import uuid
from django.db import models


# Create your models here.
class diamond(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    carat = models.FloatField(blank=True, null=True)
    cut = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    clarity = models.CharField(max_length=50, blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    table = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)