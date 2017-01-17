from rest_framework import viewsets
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .serializers import EventSerializer
from .models import Event


class EventViewSet(CacheResponseMixin, viewsets.ReadOnlyModelViewSet):

    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.related_objects.all()
        return queryset
