from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Menu, Price, Category, Set, Group, MenuSet


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('count', 'measure', 'value')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'code')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', )


class MenuSetSerializer(serializers.ModelSerializer):
    pk = serializers.ReadOnlyField(source='menu.pk')
    name = serializers.ReadOnlyField(source='menu.name')

    class Meta:
        model = MenuSet
        fields = ('pk', 'name', 'menu_count')


class SetSerializer(serializers.ModelSerializer):
    menu = MenuSetSerializer(source='menuset_set', many=True)
    photo = VersatileImageFieldSerializer(sizes='set_photo')
    prices = PriceSerializer(many=True, read_only=True)

    class Meta:
        model = Set
        fields = ('pk', 'name', 'description', 'created_at', 'menu', 'prices', 'photo')


class MenuSerializer(serializers.ModelSerializer):
    photo = VersatileImageFieldSerializer(sizes='menu_photo')
    prices = PriceSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Menu
        fields = ('pk', 'name', 'description', 'category', 'created_at', 'detail', 'prices', 'photo')
