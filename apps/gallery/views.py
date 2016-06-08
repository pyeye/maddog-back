from rest_framework import viewsets

from .serializers import ImageSerializer, AlbumSerializer
from .models import Image, Album


class ImageViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Image.objects.filter(album=None)
    serializer_class = ImageSerializer


class AlbumViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
