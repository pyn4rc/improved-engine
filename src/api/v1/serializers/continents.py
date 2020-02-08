from cities.models import Continent
from rest_framework import serializers


class ContinentSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = '__all__'


class ContinentListSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = ('id', 'name', )
