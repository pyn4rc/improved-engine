from cities.models import Country
from rest_framework.viewsets import ModelViewSet

from api.v1.serializers.countries import CountrySerializerV1, CountryListSerializerV1


class CountryViewSetV1(ModelViewSet):
    queryset = Country.objects.all().order_by('-population')
    serializer_class = CountrySerializerV1

    def get_serializer_class(self):
        if self.action == 'list':
            return CountryListSerializerV1
        return super().get_serializer_class()
