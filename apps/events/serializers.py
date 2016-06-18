from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Event, Artist


class ArtistSerializer(serializers.ModelSerializer):
    img = VersatileImageFieldSerializer(sizes='artist_img')

    class Meta:
        model = Artist
        fields = ('name', 'style', 'img')


class EventSerializer(serializers.ModelSerializer):
    poster = VersatileImageFieldSerializer(sizes='event_poster')
    artists = ArtistSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('pk', 'name', 'artists', 'info', 'date', 'start',
                  'discounts', 'price', 'is_special', 'poster', 'extra')
