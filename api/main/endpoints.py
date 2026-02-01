from .class_api import (
    TypeOfServiceViewSet,
    ServiceViewSet,
    MasterViewSet,
    GalleryViewSet,
    ReviewViewSet,
    SignUpViewSet,
)
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'typeofservice', TypeOfServiceViewSet, basename='typeofservice')
router.register(r'services', ServiceViewSet, basename='services')
router.register(r'masters', MasterViewSet, basename='masters')
router.register(r'galleries', GalleryViewSet, basename='galleries')
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'signup', SignUpViewSet, basename='signup')


urlpatterns = [
    path('', include(router.urls)), 
]