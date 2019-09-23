from rest_framework.viewsets import ModelViewSet

from car.models import Manufacturer, CarModel, Car
from car.serializers import ManufacturerSerializer, CarModeSerializer, CarSerializer


class ManufacturerViewSet(ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class CarModelViewSet(ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModeSerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
