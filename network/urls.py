from network.views import ContactViewSet, ProductViewSet, SupplierViewSet 
from rest_framework.routers import DefaultRouter
from network.apps import NetworkConfig


app_name = NetworkConfig.name
router = DefaultRouter()
router.register(r'supplier', SupplierViewSet, basename='supplier')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'contact', ContactViewSet, basename='contact')

urlpatterns = router.urls
