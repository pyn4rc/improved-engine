from cities.models import Region
from rest_framework import serializers


class RegionSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class RegionListSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name', )
