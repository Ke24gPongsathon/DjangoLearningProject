import django_filters

from apis.models import User, Address

from apis import utils
from django.db.models import F, Q, CharField,DateTimeField, ExpressionWrapper,Value as V
from django.db.models.functions import Concat
from datetime import timedelta


FILTER_CHOICES = [
    ('exact', 'Equals'),
    ('gt', 'Greater than'),
    ('lt', 'Less than'),
]

class UserFilter(django_filters.FilterSet):
    # created_at = django_filters.DateFromToRangeFilter(field_name='created_at')
    email = django_filters.CharFilter(field_name='email', lookup_expr='icontains')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    citizen_id = django_filters.CharFilter(field_name='citizen_id', lookup_expr='exact')
    gender = django_filters.ChoiceFilter(field_name='gender', choices=utils.GENDER_CHOICE)

    # search = django_filters.CharFilter(method='search_user')
    # def search_user(self, queryset, name, value):
    #     return queryset.filter(
    #         Q(email__icontains=value) | Q(first_name__icontains=value) | Q(last_name__icontains=value) | Q(
    #             position__icontains=value) | Q(username__icontains=value) | Q(phone__icontains=value)
    #     )

    class Meta:
        model = User
        fields = [
            'created_at',
            'email', 'name', 'citizen_id', 'gender', 'search',
        ]
        