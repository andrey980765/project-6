# core/urls.py
from django.urls import path, include
from rest_framework import routers
from .views import ClientViewSet, ProjectViewSet, BuildingViewSet, ContractorViewSet

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'buildings', BuildingViewSet)
router.register(r'contractors', ContractorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
