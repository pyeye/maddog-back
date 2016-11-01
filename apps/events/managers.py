from datetime import datetime, timedelta

from django.db import models


class EventsManager(models.Manager):

    def get_queryset(self):
        return super(EventsManager, self).get_queryset().prefetch_related('artists').filter(
            is_active=True,
            date__gte=datetime.now(),
            date__lte=datetime.now() + timedelta(days=30)
        ).order_by('date')