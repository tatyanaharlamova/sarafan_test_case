from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from store.models import Category, Subcategory, Product, Cart
from store.pagination import CustomPagination
from store.serializer import CategorySerializer, SubcategorySerializer, ProductSerializer, CartSerializer
from users.permissions import IsOwner


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
    serializer_class = CartSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Cart.objects.filter(owner=self.request.user.pk).order_by("id")

    def perform_create(self, serializer):
        cart = serializer.save()
        cart.owner = self.request.user
        cart.save()

    def get_permissions(self):
        if self.action in ['create', 'retrieve']:
            self.permission_classes = (IsAuthenticated,)
        elif self.action in ['update', 'destroy']:
            self.permission_classes = (IsOwner,)
        return super().get_permissions()


@api_view(['DELETE'])
def clean_all(request):
    if request.method == 'DELETE':
        carts = Cart.objects.filter(owner=request.user.pk)
        for product in carts:
            product.delete()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def my_cart(request):
    if request.method == 'GET':
        carts = Cart.objects.filter(owner=request.user.pk)
        sum_ = 0
        product_dict = {}
        for cart in carts:
            sum_ += cart.product.price
            if cart.product.name in product_dict.keys():
                product_dict[cart.product.name] += 1
            else:
                product_dict[cart.product.name] = 1
        num = len(carts)
        return Response({"Количество позиций": num, "Сумма": sum_, "Товары": product_dict})
