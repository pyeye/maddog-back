from rest_framework import serializers

from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('date', 'time', 'is_vip', 'phone_number', 'name', 'count_people', 'comment')
