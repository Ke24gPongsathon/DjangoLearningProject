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
    # --------------Date---------------- #
    created_at = django_filters.DateFromToRangeFilter(field_name='created_at')
    # --------------User---------------- #
    created_by = django_filters.ModelChoiceFilter(field_name='user', queryset=User.objects.all())
    # --------------Status---------------- #
    # --------------Text---------------- #
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    # --------------Other---------------- #
    company = django_filters.ModelChoiceFilter(field_name='company', queryset=Company.objects.all())
    is_verified = django_filters.BooleanFilter(field_name='is_verified')
    search = django_filters.CharFilter(method='search_user')

    def search_user(self, queryset, name, value):
        return queryset.filter(
            Q(email__icontains=value) | Q(first_name__icontains=value) | Q(last_name__icontains=value) | Q(
                position__icontains=value) | Q(username__icontains=value) | Q(phone__icontains=value)
        )

    class Meta:
        model = User
        fields = [
            'created_at', 'last_login', 'created_by', 'email', 'first_name',
            'last_name', 'position', 'company', 'is_verified', 'search',
        ]