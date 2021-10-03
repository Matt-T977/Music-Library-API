from django.db import models
from django.db.models.fields import BooleanField, CharField, IntegerField

# Create your models here.
class Song(models.Model):
    title = CharField(max_length=50)
    artist = CharField(max_length=50)
    album = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    genre = CharField(max_length=50)
    number_of_likes = IntegerField(default=0)
    number_of_dislikes = IntegerField(default=0)