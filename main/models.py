from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from django.contrib.auth.models import User

from autosalon_project import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class ProductType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    description = models.TextField(blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^\+375\s\(\d{2}\)\s\d{3}-\d{2}-\d{2}$', message="Телефон должен быть в формате +375 (XX) XXX-XX-XX")
    phone = models.CharField(validators=[phone_regex], max_length=20)
    city = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.full_name

class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.full_name} ({self.position})"

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateField(auto_now_add=True)
    delivery_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Заказ {self.id} - {self.product.name} для {self.client.full_name}"

from django.db import models

class FAQ(models.Model):
    question = models.CharField("Вопрос", max_length=200)
    answer = models.TextField("Ответ")
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)

    def __str__(self):
        return self.question

from django.db import models

class Contact(models.Model):
    name = models.CharField("Имя", max_length=100)
    photo = models.ImageField("Фото", upload_to='contacts/')
    job_description = models.TextField("Описание работы")
    email = models.EmailField("Почта")
    phone = models.CharField("Телефон", max_length=20)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.name