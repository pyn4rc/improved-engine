from cities.models import City
from rest_framework import serializers


class CitySerializerV1(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CityListSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', )
