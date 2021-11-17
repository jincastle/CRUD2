from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField(auto_now=False, null=True)
    movies = models.ManyToManyField('Movie', through='Actor_Movie')
    class Meta:
        db_table="actors"


class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField(auto_now=False, null=True)
    running_time = models.TimeField(auto_now=False, null=True)
    class Meta:
        db_table="movies"

class Actor_Movie(models.Model):
    actors = models.ForeignKey('Actor', on_delete=models.CASCADE)
    movies = models.ForeignKey('Movie', on_delete=models.CASCADE)