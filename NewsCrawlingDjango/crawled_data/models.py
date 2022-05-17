from django.db import models

# Create your models here.
# class BoardData(models.Model):
#     date = models.CharField(max_length=50, null=True, default='')
#     title = models.CharField(max_length=300)
#     link = models.URLField()

#     def __str__(self):
#         return self.title

class UserInput(models.Model):
    startdate = models.CharField(max_length = 8)
    finishdate = models.CharField(max_length = 8)

    def __str__(self):
        return self.startdate +'>>'+ self.finishdate

# class WordCloud(models.Model):
#     cloud = models.CharField(max_length = 10)