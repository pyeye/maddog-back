from rest_framework import viewsets, generics
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .serializers import MenuSerializer, SetSerializer, CategorySerializer
from .models import Menu, Set, Category
from apps.base.renderers import MDMenuRenderer


class MenuViewSet(CacheResponseMixin, viewsets.ReadOnlyModelViewSet):

    serializer_class = MenuSerializer
    renderer_classes = (MDMenuRenderer, JSONRenderer, BrowsableAPIRenderer)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Menu.related_objects.filter(is_active=True)
        group = self.request.query_params.get('group', None)
        if group is not None:
            queryset = queryset.filter(category__group__code=group)
        return queryset


class CategoryAPIView(generics.ListAPIView):

    serializer_class = CategorySerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Category.objects.all()
        group = self.request.query_params.get('group', None)
        if group is not None:
            queryset = queryset.filter(group__code=group)
        return queryset


class SetViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Set.objects.filter(is_active=True)
    serializer_class = SetSerializer
