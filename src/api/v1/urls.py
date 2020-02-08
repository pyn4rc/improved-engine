from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.v1.views.alt_names import AltNamesViewSetV1
from api.v1.views.cities import CityViewSetV1
from api.v1.views.continents import ContinentViewSetV1
from api.v1.views.countries import CountryViewSetV1
from api.v1.views.districts import DistrictViewSetV1
from api.v1.views.postal_codes import PostalCodeViewSetV1
from api.v1.views.regions import RegionViewSetV1
from api.v1.views.subregions import SubregionViewSetV1

router = DefaultRouter()
router.register('cities', CityViewSetV1)
router.register('countries', CountryViewSetV1)
router.register('regions', RegionViewSetV1)
router.register('alt-names', AltNamesViewSetV1)
router.register('continents', ContinentViewSetV1)
router.register('subregions', SubregionViewSetV1)
router.register('districts', DistrictViewSetV1)
router.register('postal-codes', PostalCodeViewSetV1)

urlpatterns = [
    path('', include(router.urls)),
]
