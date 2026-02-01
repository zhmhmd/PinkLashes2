from django_filters import FilterSet, CharFilter, NumberFilter, DateFilter, TimeFilter
from main.models import Service, Master, Gallery, Review, TypeOfService, SignUp


class ServiceFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Service
        fields = ['name',]


class MasterFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    position = CharFilter(field_name='position', lookup_expr='iexact')
    experience = CharFilter(field_name='experience', lookup_expr='icontains')
    services = CharFilter(field_name='services__name', lookup_expr='icontains')

    class Meta:
        model = Master
        fields = ['name', 'position', 'experience', 'services',]
        
    
class GalleryFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Gallery
        fields = ['name']


class ReviewFilter(FilterSet):
    master_name = CharFilter(field_name='master__name', lookup_expr='icontains')
    score = NumberFilter(field_name='score', lookup_expr='iexact')

    class Meta:
        model = Review
        fields = ['master_name', 'score',]


class TypeOfServiceFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    price_min = NumberFilter(field_name='price', lookup_expr='gte')
    price_max = NumberFilter(field_name='price', lookup_expr='lte')
    master_name = CharFilter(field_name='master__name', lookup_expr='icontains')

    class Meta:
        model = TypeOfService
        fields = ['title', 'price_min', 'price_max', 'master_name']


class SignUpFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    services = CharFilter(field_name='services__name', lookup_expr='icontains')
    master_name = CharFilter(field_name='master__name', lookup_expr='icontains')
    date = DateFilter(field_name='date', lookup_expr='exact')
    time = TimeFilter(field_name='time', lookup_expr='exact')

    class Meta:
        model = SignUp
        fields = ['name', 'services', 'master_name',
                'date', 'time',]