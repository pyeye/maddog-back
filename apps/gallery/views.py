from rest_framework import generics
from rest_framework_extensions.cache.decorators import cache_response

from .serializers import GallerySerializer, AlbumSerializer
from .models import Album


class AlbumAPIView(generics.RetrieveAPIView):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    @cache_response()
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class GalleryAPIView(generics.ListAPIView):

    serializer_class = GallerySerializer

    @cache_response()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Album.related_objects.all()
        return queryset
