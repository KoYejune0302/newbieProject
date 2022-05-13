from django.db import models

# Create your models here.
class BoardData(models.Model):
    date = models.CharField(max_length=10)
    title = models.CharField(max_length=300)
    link = models.URLField()