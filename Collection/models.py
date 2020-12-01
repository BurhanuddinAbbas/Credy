from django.db import models
from Movie.models import Movie
import uuid


class Collection(models.Model):
    title = models.CharField(max_length=200, null=True, blank=False)
    description = models.CharField(max_length=500, null=True, blank=False)
    movies = models.ManyToManyField(Movie, related_name='movies', blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
