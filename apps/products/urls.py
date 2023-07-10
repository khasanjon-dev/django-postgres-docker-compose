from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import ProductModelViewSet

router = DefaultRouter()
router.register('', ProductModelViewSet, 'products')

urlpatterns = [
    path('', include(router.urls)),
]
