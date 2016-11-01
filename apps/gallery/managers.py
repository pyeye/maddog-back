from django.db import models


class GalleryManager(models.Manager):

    def get_queryset(self):
        return super(GalleryManager, self).get_queryset().prefetch_related('images').select_related('event')
