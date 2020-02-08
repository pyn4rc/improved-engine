from cities.models import City
from rest_framework.viewsets import ModelViewSet

from api.v1.serializers.cities import CitySerializerV1, CityListSerializerV1


class CityViewSetV1(ModelViewSet):
    queryset = City.objects.all().order_by('-population')
    serializer_class = CitySerializerV1

    def get_serializer_class(self):
        if self.action == 'list':
            return CityListSerializerV1
        return super().get_serializer_class()
