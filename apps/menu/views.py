from rest_framework import viewsets

from .serializers import MenuSerializer
from .models import Menu

class MenuViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Menu.objects.filter(is_active=True)
    serializer_class = MenuSerializer
