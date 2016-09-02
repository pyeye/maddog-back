from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Album, Image
from apps.events.models import Event


class GalleryEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'info', 'date')


class ImageSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes='gallery_image')

    class Meta:
        model = Image
        fields = ('image', )


class AlbumSerializer(serializers.ModelSerializer):
    main_image = VersatileImageFieldSerializer(sizes='album_image')
    images = ImageSerializer(many=True, read_only=True)
    event = GalleryEventSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ('pk', 'name', 'description', 'event', 'main_image', 'images')


class GallerySerializer(serializers.ModelSerializer):
    main_image = VersatileImageFieldSerializer(sizes='album_image')
    event = GalleryEventSerializer(read_only=True)
    image_count = serializers.IntegerField(source='images.count', read_only=True)

    class Meta:
        model = Album
        fields = ('pk', 'name', 'description', 'event', 'main_image', 'image_count')
