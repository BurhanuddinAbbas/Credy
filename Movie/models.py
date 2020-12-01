from django.db import models
import uuid


class Movie(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    genres = models.CharField(max_length=200, default="", null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4)
