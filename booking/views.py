from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from booking import serializers
from booking import models


class MechanicViewSet(ModelViewSet):
    serializer_class = serializers.MechanicSerializer
    queryset = models.Mechanic.objects.all()


class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        if self.request.method == 'GET':
            return models.Booking.objects.select_related()
        return models.Booking.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.BookingSerializerGet
        return serializers.BookingSerializer
