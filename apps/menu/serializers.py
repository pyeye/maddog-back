from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Menu, Price, Category


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('count', 'measure', 'value')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class MenuSerializer(serializers.ModelSerializer):
    photo = VersatileImageFieldSerializer(sizes='menu_photo')
    prices = PriceSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Menu
        fields = ('pk', 'name', 'description', 'category', 'detail', 'prices', 'is_lunch', 'photo')
