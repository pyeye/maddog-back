from rest_framework.generics import CreateAPIView

from .serializers import ReservationSerializer


class ReservationAPIView(CreateAPIView):
    serializer_class = ReservationSerializer
