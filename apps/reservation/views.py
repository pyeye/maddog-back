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
        # send_mail(
        #     'Новая бронь',
        #     'Проверь админку',
        #     settings.EMAIL_HOST_USER,
        #     ['arturka-74@mail.ru', settings.EMAIL_HOST_USER],
        #     fail_silently=False
        # )
