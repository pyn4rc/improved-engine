from cities.models import Continent
from rest_framework.viewsets import ModelViewSet

from api.v1.serializers.continents import ContinentSerializerV1, ContinentListSerializerV1


class ContinentViewSetV1(ModelViewSet):
    queryset = Continent.objects.all().order_by('-id')
    serializer_class = ContinentSerializerV1

    def get_serializer_class(self):
        if self.action == 'list':
            return ContinentListSerializerV1
        return super().get_serializer_class()
