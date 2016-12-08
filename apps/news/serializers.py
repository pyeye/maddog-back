from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import News, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', )


class NewsSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes='news_image')
    category = CategorySerializer(read_only=True)

    class Meta:
        model = News
        fields = ('pk', 'title', 'description', 'category', 'created_at', 'updated_at', 'image', 'extra')
