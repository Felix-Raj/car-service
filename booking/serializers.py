from rest_framework.serializers import ModelSerializer

from booking.models import Mechanic, Booking


class MechanicSerializer(ModelSerializer):
    class Meta:
        model = Mechanic
        fields = '__all__'


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class BookingSerializerGet(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        depth = 1
