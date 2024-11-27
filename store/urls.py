from django.urls import path
from rest_framework.routers import SimpleRouter

from store.apps import StoreConfig
from store.views import CartViewSet, CategoryListAPIView, SubcategoryListAPIView, \
    ProductListAPIView, clean_all, my_cart

app_name = StoreConfig.name

router = SimpleRouter()
router.register('carts', CartViewSet, basename='carts')

urlpatterns = [
    path("", CategoryListAPIView.as_view(), name="categories"),
    path("subcategories/", SubcategoryListAPIView.as_view(), name="subcategories"),
    path("products/", ProductListAPIView.as_view(), name="products"),
    path("clean/", clean_all, name="clean_all"),
    path("my_cart/", my_cart, name="my_cart")
]
urlpatterns += router.urls
