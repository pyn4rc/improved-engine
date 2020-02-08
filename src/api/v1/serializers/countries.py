from cities.models import Country
from rest_framework import serializers


class CountrySerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CountryListSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', )
