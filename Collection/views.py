from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from collections import OrderedDict
from Collection.models import Collection
from Collection.serializers import CollectionSerializer
from rest_framework import permissions
import pandas as pd
import numpy as np
from Movie.models import Movie
from Movie.serializers import MovieSerializer


class CollectionViewSet(CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView):
    queryset = Collection.objects.none()
    lookup_field = 'uuid'
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.collections.all()

    def get(self, request, *args, **kwargs):
        fav_genres = OrderedDict()
        fav_genres['favourite_genres'] = pd.value_counts(
            np.array([i.split(',') for i in
                      self.request.user.collections.all().values_list('movies__genres', flat=True)]).flatten())[
                                         :3].index.tolist()
        response_object = self.list(request, *args, **kwargs)
        response_object.data.append(fav_genres)
        return response_object

    def post(self, request, *args, **kwargs):
        dispatch_response = self.create(request, *args, **kwargs)
        dispatch_response.data = {'uuid': dispatch_response.data['uuid']}
        return dispatch_response

    def put(self, request, *args, **kwargs):
        dispatch_response = self.update(request, *args, **kwargs)
        dispatch_response.data.pop('uuid')
        return dispatch_response
