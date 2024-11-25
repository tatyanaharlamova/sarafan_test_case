from django.db import models

from users.models import User


class Category(models.Model):
    """Категория."""
    title = models.CharField(
        max_length=100, verbose_name="Название", help_text="Укажите название категории"
    )
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    preview = models.ImageField(
        upload_to="store/category",
        verbose_name="Изображение",
        blank=True,
        null=True,
        help_text="Добавьте изображение",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Subcategory(models.Model):
    """Подкатегория."""
    title = models.CharField(max_length=50, verbose_name="Название", help_text="Укажите название подкатегории",
                             blank=True, null=True)
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        related_name='subcategories',
        verbose_name='Подкатегория',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    """Продукт."""
    name = models.CharField(
        max_length=100, verbose_name="Название", help_text="Укажите название продукта"
    )
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    category = models.ForeignKey(
        Category,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='products')
    subcategory = models.ForeignKey(
        Subcategory,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='products')
    image_front = models.ImageField(
        upload_to="store/products",
        verbose_name="Изображение спереди",
        blank=True,
        null=True,
        help_text="Добавьте изображение спереди",
    )
    image_side = models.ImageField(
        upload_to="store/products",
        verbose_name="Изображение сбоку",
        blank=True,
        null=True,
        help_text="Добавьте изображение сбоку",
    )
    image_back = models.ImageField(
        upload_to="store/products",
        verbose_name="Изображение сзади",
        blank=True,
        null=True,
        help_text="Добавьте изображение сзади",
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена", help_text="Укажите цену продукта"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Cart(models.Model):
    """Корзина."""
    product = models.ForeignKey(
        Product,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='products',
        verbose_name='Товар'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='users',
        verbose_name='Пользователь',
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return self.product.name
