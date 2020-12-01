from rest_framework import serializers

from Collection.models import Collection
from Movie.models import Movie
from Movie.serializers import MovieSerializer


def key_error_handler(source: dict, pop_key: str):
    try:
        return source.pop(pop_key)
    except KeyError:
        return []


class CollectionSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200, required=True)
    description = serializers.CharField(max_length=500, required=False)
    movies = MovieSerializer(many=True, required=False)
    uuid = serializers.UUIDField(read_only=True)

    class Meta:
        model = Collection
        fields = ['title', 'description', 'movies', 'uuid']

    def create(self, validated_data):
        movies_data_list = key_error_handler(validated_data, 'movies')
        instance = super(CollectionSerializer, self).create(validated_data)
        self.context['request'].user.collections.add(instance)
        for movie_dict in movies_data_list:
            key_error_handler(movie_dict, 'uuid')
            movie_instance = Movie.objects.create(**movie_dict)
            instance.movies.add(movie_instance)
        return instance

    def update(self, instance, validated_data):
        try:
            for movie_data in validated_data.pop('movies'):
                movie_data = dict(movie_data)
                movie_obj = Movie.objects.get(uuid=movie_data.pop('uuid'))
                movie_obj.__dict__.update(movie_data)
                movie_obj.save()
        except KeyError:
            pass
        return super(CollectionSerializer, self).update(instance=instance, validated_data=validated_data)
