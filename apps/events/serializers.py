from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    poster = VersatileImageFieldSerializer(sizes='event_poster')

    class Meta:
        model = Event
        fields = ('pk', 'name', 'artists', 'style', 'info', 'date', 'start',
                  'discounts', 'price', 'is_special', 'poster', 'extra')
