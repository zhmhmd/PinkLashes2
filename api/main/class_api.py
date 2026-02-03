from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import StandardResultsSetPagination
from main.models import TypeOfService, Service, Master, Review, Gallery, SignUp
from .serializers import (
    TypeOfServiceSerializers,
    ServiceSerializers,
    MasterSerializers,
    ReviewSerializers,
    GallerySerializers,
    SignUpSerializers,
)
from .filters import (
    TypeOfServiceFilter,
    ServiceFilter,
    MasterFilter,
    ReviewFilter,
    GalleryFilter,
    SignUpFilter,
)


class TypeOfServiceViewSet(ReadOnlyModelViewSet):
    queryset = TypeOfService.objects.all()
    serializer_class = TypeOfServiceSerializers
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = TypeOfServiceFilter

    def get_permissions(self):
        return [AllowAny()]
    

class ServiceViewSet(ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServiceFilter

    def get_permissions(self):
        return [AllowAny()]
    

class MasterViewSet(ReadOnlyModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializers
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = MasterFilter

    def get_permissions(self):
        return [AllowAny()]
    

class GalleryViewSet(ReadOnlyModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializers
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = GalleryFilter

    def get_permissions(self):
        return [AllowAny()]
    

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReviewFilter

    def get_permissions(self):
        if self.action in ['create',]:
            pass
        return [IsAuthenticated()]
    

class SignUpViewSet(ModelViewSet):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializers
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = SignUpFilter

    def get_permissions(self):
        if self.action in ['create',]:
            pass
        return [IsAuthenticated()]