from datetime import datetime, timedelta
from rest_framework import viewsets

from .serializers import EventSerializer
from .models import Event


class EventViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.filter(is_active=True, date__gte=datetime.now()).order_by('date')
        is_special = self.request.query_params.get('special', None)
        is_regular = self.request.query_params.get('regular', None)
        if is_special is not None:
            queryset = queryset.filter(date__lte=datetime.now() + timedelta(days=30), is_special=True)
        if is_regular is not None:
            queryset = queryset.filter(date__lte=datetime.now() + timedelta(days=14), is_special=False)
        return queryset
