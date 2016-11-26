from rest_framework.generics import CreateAPIView
from django.core.mail import send_mail
from django.conf import settings

from apps.base.auth import UnsafeSessionAuthentication

from .serializers import FeedbackSerializer


class FeedbackAPIView(CreateAPIView):
    serializer_class = FeedbackSerializer
    authentication_classes = (UnsafeSessionAuthentication,)

    def perform_create(self, serializer):
        serializer.save()
        send_mail(
            'Новый отзыв',
            'https://maddogclub.com/api/v1/admin/feedback/feedback/' + serializer.pk + '/change/',
            settings.EMAIL_HOST_USER,
            ['feedback@maddogclub.com'],
            fail_silently=False
        )

