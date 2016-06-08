from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Menu, Price


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('count', 'measure', 'value')


class MenuSerializer(serializers.ModelSerializer):
    photo = VersatileImageFieldSerializer(sizes='menu_photo')
    prices = PriceSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ('pk', 'name', 'description', 'detail', 'prices', 'is_lunch', 'photo')
