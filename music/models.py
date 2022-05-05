from django.db import models

# Create your models here.

class Music(models.Model):
    title = models.CharField(max_length= 300)
    artist = models.CharField(max_length= 300)
    album = models.CharField(max_length= 300)
    release_date = models.DateField()
    genre = models.CharField(max_length= 300)
