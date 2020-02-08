from cities.models import PostalCode
from rest_framework import serializers


class PostalCodeSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = PostalCode
        fields = '__all__'


class PostalCodeListSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = PostalCode
        fields = ('id', 'name', )
