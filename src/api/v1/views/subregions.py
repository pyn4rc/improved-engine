from cities.models import Subregion
from rest_framework.viewsets import ModelViewSet

from api.v1.serializers.subregions import SubregionSerializerV1, SubregionListSerializerV1


class SubregionViewSetV1(ModelViewSet):
    queryset = Subregion.objects.all()
    serializer_class = SubregionSerializerV1

    def get_serializer_class(self):
        if self.action == 'list':
            return SubregionListSerializerV1
        return super().get_serializer_class()
