import django_filters

from apis.models import User, Address

from apis import utils
from django.db.models import F, Q, CharField,DateTimeField, ExpressionWrapper,Value as V
from django.db.models.functions import Concat
from datetime import timedelta



class UserFilter(django_filters.FilterSet):
    created_at = django_filters.DateFromToRangeFilter(field_name='created_at')
    email = django_filters.CharFilter(lookup_expr='icontains')
    name = django_filters.CharFilter(lookup_expr='icontains')
    citizen_id = django_filters.CharFilter(lookup_expr='icontains')
    gender = django_filters.ChoiceFilter(choices=utils.GENDER_CHOICE)

    address__house_number = django_filters.CharFilter(lookup_expr='icontains')
    address__village = django_filters.CharFilter(lookup_expr='icontains')
    address__road = django_filters.CharFilter(lookup_expr='icontains')
    address__sub_district = django_filters.CharFilter(lookup_expr='icontains')
    address__district = django_filters.CharFilter(lookup_expr='icontains')
    address__province = django_filters.CharFilter(lookup_expr='icontains')
    address__zip_code = django_filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = User
        fields = [
            'created_at',
            'email', 'name', 'citizen_id', 'gender',
            'address__house_number', 'address__village',
            'address__road', 'address__sub_district',
            'address__district', 'address__province',
            'address__house_number', 'address__village',
            'address__zip_code',
        ]
        