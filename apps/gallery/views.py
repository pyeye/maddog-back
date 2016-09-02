from rest_framework import generics

from .serializers import GallerySerializer, AlbumSerializer
from .models import Album


class AlbumAPIView(generics.RetrieveAPIView):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class GalleryAPIView(generics.ListAPIView):

    queryset = Album.objects.all()
    serializer_class = GallerySerializer
