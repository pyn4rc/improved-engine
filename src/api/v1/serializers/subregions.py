from cities.models import Subregion
from rest_framework import serializers


class SubregionSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Subregion
        fields = '__all__'


class SubregionListSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Subregion
        fields = ('id', 'name', )
