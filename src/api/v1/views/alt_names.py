from cities.models import AlternativeName
from rest_framework.viewsets import ModelViewSet

from api.v1.serializers.alt_names import AltNamesSerializerV1, AltNamesListSerializerV1


class AltNamesViewSetV1(ModelViewSet):
    queryset = AlternativeName.objects.all().order_by('-id')
    serializer_class = AltNamesSerializerV1

    def get_serializer_class(self):
        if self.action == 'list':
            return AltNamesListSerializerV1
        return super().get_serializer_class()
