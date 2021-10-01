from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Song(models.Model):
    title = CharField(max_length=50)
    artist = CharField(max_length=50)
    album = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    genre = CharField(max_length=50)