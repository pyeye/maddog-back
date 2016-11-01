from rest_framework import viewsets

from .serializers import EventSerializer
from .models import Event


class EventViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.related_objects.all()
        return queryset
