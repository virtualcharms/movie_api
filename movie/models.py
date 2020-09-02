from django.db import models

# Create your models here.


class Movie(models.Model):
    photo_url = models.TextField()
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    actors = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}, {self.genre}, {self.director}, {self.actors}, {self.description}'
