from cities.models import Region
from rest_framework.viewsets import ModelViewSet

from api.v1.serializers.regions import RegionSerializerV1, RegionListSerializerV1


class RegionViewSetV1(ModelViewSet):
    queryset = Region.objects.all().order_by('-id')
    serializer_class = RegionSerializerV1

    def get_serializer_class(self):
        if self.action == 'list':
            return RegionListSerializerV1
        return super().get_serializer_class()
