from cities.models import District
from rest_framework.viewsets import ModelViewSet

from api.v1.serializers.districts import DistrictSerializerV1, DistrictListSerializerV1


class DistrictViewSetV1(ModelViewSet):
    queryset = District.objects.all().order_by('-population')
    serializer_class = DistrictSerializerV1

    def get_serializer_class(self):
        if self.action == 'list':
            return DistrictListSerializerV1
        return super().get_serializer_class()
