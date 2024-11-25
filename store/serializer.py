from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from store.models import Category, Subcategory, Product, Cart


class SubcategorySerializer(ModelSerializer):
    class Meta:
        model = Subcategory
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    subcategories = SerializerMethodField()

    def get_subcategories(self, category):
        return [sub.title for sub in Subcategory.objects.filter(category=category)]

    class Meta:
        model = Category
        fields = ("id", "title", "preview", "slug", "subcategories")


class ProductSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
