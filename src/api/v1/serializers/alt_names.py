from cities.models import AlternativeName
from rest_framework import serializers


class AltNamesSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = AlternativeName
        fields = '__all__'


class AltNamesListSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = AlternativeName
        fields = ('id', 'name', )
