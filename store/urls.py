from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter

from store.apps import StoreConfig
from store.views import CartViewSet, CategoryListAPIView, SubcategoryListAPIView, \
    ProductListAPIView

app_name = StoreConfig.name

router = SimpleRouter()
router.register('carts', CartViewSet, basename='carts')

urlpatterns = [
    path("", CategoryListAPIView.as_view(), name="categories"),
    path("subcategories/", SubcategoryListAPIView.as_view(), name="subcategories"),
    path("products/", ProductListAPIView.as_view(), name="products"),
]
urlpatterns += router.urls
