from django.db import models

# Create your models here.
class BoardData(models.Model):
    start = models.CharField(max_length=10, null = 'True')
    finish = models.CharField(max_length=10, null = 'True')
    title = models.CharField(max_length=300)
    link = models.URLField()


    def __str__(self):
        return self.title

class UserInput(models.Model):
    startdate = models.CharField(max_length = 8)
    finishdate = models.CharField(max_length = 8)

    def __str__(self):
        return self.startdate +'>>'+ self.finishdate