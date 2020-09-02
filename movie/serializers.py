from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'photo_url', 'title', 'genre',
                  'director', 'actors', 'description')
