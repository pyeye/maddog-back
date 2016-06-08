from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Album, Image


class ImageSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes='gallery_image')

    class Meta:
        model = Image
        fields = ('info', 'created_at', 'image')


class AlbumSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('pk', 'name', 'description', 'images')
