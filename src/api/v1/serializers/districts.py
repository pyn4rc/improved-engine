from cities.models import District
from rest_framework import serializers


class DistrictSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class DistrictListSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name', )
