from django.core.mail import send_mail
from django.conf import settings
from rest_framework.generics import CreateAPIView

from .serializers import ReservationSerializer

from apps.base.auth import UnsafeSessionAuthentication


class ReservationAPIView(CreateAPIView):
    serializer_class = ReservationSerializer
    authentication_classes = (UnsafeSessionAuthentication,)

    def perform_create(self, serializer):
        serializer.save()
        send_mail(
            'Новая бронь',
            'Проверь админку',
            'reservation@maddogclub.com',
            fail_silently=False
        )
