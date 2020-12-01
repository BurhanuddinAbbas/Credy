from requests.auth import HTTPBasicAuth
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
import requests
from Collection.models import Collection
from Credy.settings import REST_PASSWORD, REST_USERNAME
from Movie.serializers import MovieSerializer, Movie


@api_view()
def list_movies(request):
    url = request.build_absolute_uri()
    while True:
        try:
            resp = requests.get('https://demo.credy.in/api/v1/maya/movies/' + url[url.find('?'):],
                                auth=HTTPBasicAuth(REST_USERNAME, REST_PASSWORD), timeout=2)
            if resp.status_code != 200:
                if resp.status_code == 404:
                    return Response(data=resp.json(), status=resp.status_code)
                else:
                    continue
            else:
                return Response(data=resp.json(), status=resp.status_code)
        except requests.exceptions.ReadTimeout:
            continue


class MovieViewSet(CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView):
    queryset = Movie.objects.none()
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Collection.objects.get(uuid=self.request.query_params.get('collection_uuid')).movies.all()
