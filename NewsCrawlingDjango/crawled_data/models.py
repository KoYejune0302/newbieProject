from django.db import models

# Create your models here.
class BoardData(models.Model):
    start = models.CharField(max_length=10, null = 'True')
    finish = models.CharField(max_length=10, null = 'True')
    title1 = models.CharField(max_length=300, null = 'True')
    link1 = models.URLField(null = 'True')
    title2 = models.CharField(max_length=300, null = 'True')
    link2 = models.URLField(null = 'True')
    title3 = models.CharField(max_length=300, null = 'True')
    link3 = models.URLField(null = 'True')
    cloud = models.ImageField(blank=True)


    def __str__(self):
        return self.title

class UserInput(models.Model):
    startdate = models.CharField(max_length = 8)
    finishdate = models.CharField(max_length = 8)

    def __str__(self):
        return self.startdate +'>>'+ self.finishdate