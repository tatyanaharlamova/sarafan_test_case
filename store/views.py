from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from store.models import Category, Subcategory, Product, Cart
from store.pagination import CustomPagination
from store.serializer import CategorySerializer, SubcategorySerializer, ProductSerializer, CartSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination
    permission_classes = (AllowAny,)


class SubcategoryListAPIView(ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    pagination_class = CustomPagination
    permission_classes = (AllowAny,)


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    permission_classes = (AllowAny,)


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        cart = serializer.save()
        cart.owner = self.request.user
        cart.save()
    