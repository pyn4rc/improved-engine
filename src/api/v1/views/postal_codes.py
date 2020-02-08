from cities.models import PostalCode
from rest_framework.viewsets import ModelViewSet

from api.v1.serializers.postal_codes import PostalCodeSerializerV1, PostalCodeListSerializerV1


class PostalCodeViewSetV1(ModelViewSet):
    queryset = PostalCode.objects.all().order_by('-id')
    serializer_class = PostalCodeSerializerV1

    def get_serializer_class(self):
        if self.action == 'list':
            return PostalCodeListSerializerV1
        return super().get_serializer_class()
