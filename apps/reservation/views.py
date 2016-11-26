from django.core.mail import send_mail
from django.conf import settings
from rest_framework.generics import CreateAPIView

from .serializers import ReservationSerializer

from apps.base.auth import UnsafeSessionAuthentication


class ReservationAPIView(CreateAPIView):
    serializer_class = ReservationSerializer
    authentication_classes = (UnsafeSessionAuthentication,)

    def perform_create(self, serializer):
        instance = serializer.save()
        send_mail(
            'Новая бронь: ' + str(instance.name),
            'https://maddogclub.com/api/v1/admin/reservation/reservation/' + str(instance.pk) + '/change/',
            settings.EMAIL_HOST_USER,
            ['reservation@maddogclub.com'],
            fail_silently=False
        )
