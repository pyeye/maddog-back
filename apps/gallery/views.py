from rest_framework import generics

from .serializers import GallerySerializer, AlbumSerializer
from .models import Album


class AlbumAPIView(generics.RetrieveAPIView):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class GalleryAPIView(generics.ListAPIView):

    serializer_class = GallerySerializer

    def get_queryset(self):
        queryset = Album.related_objects.all()
        return queryset
