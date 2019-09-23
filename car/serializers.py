from rest_framework.serializers import ModelSerializer

from car.models import Manufacturer, CarModel, Car


class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class CarModeSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
