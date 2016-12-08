from rest_framework import viewsets

from .serializers import NewsSerializer
from .models import News


class NewsViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = NewsSerializer

    def get_queryset(self):
        queryset = News.related_objects.all()
        return queryset
