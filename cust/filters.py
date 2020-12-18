import django_filters
from .models import *
from django_filters import DateFilter, CharFilter
from .forms import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_create", lookup_expr='gte')
    end_date = DateFilter(field_name="date_create", lookup_expr='lte')
    Note = CharFilter(field_name='note', lookup_expr='icontains')


    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_create']