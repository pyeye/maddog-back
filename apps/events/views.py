from rest_framework import viewsets

from .serializers import EventSerializer
from .models import Event


class EventViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Event.objects.filter(is_active=True)
    serializer_class = EventSerializer
