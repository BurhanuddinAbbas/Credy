from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework import serializers
from .models import *


class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200, required=True)
    description = serializers.CharField(max_length=500, required=False)
    uuid = serializers.UUIDField(required=False)
    genres = serializers.CharField(max_length=200, required=True)

    class Meta:
        model = Movie
        fields = ['title', 'description', 'uuid', 'genres']

    def create(self, validated_data):
        super(MovieSerializer).create(validated_data)

    def update(self, instance, validated_data):
        super(MovieSerializer, self).update(validated_data=validated_data, instance=instance)
