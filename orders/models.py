from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name="Category")

    def __str__(self):
        return f"{ self.name }"


class Topping(models.Model):
    name = models.CharField(max_length=64, default='')

    def __str__(self):
        return f"{self.name}"


class ExtraSub(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Price(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.price}"


class Size(models.Model):
    size = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.size}"


class ToppingNumber(models.Model):
    number = models.CharField(max_length=64, verbose_name="Number of toppings")

    def __str__(self):
        return f"{self.number}"


class PizzaType(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.type}"


class Food(models.Model):
    name = models.CharField(max_length=64, verbose_name="Food")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='food_category')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='food_size', blank=True, null=True)
    type = models.ForeignKey(PizzaType, on_delete=models.CASCADE, related_name='pizza_type', blank=True, null=True)
    select_toppings = models.ForeignKey(ToppingNumber, on_delete=models.CASCADE, related_name='pizza_topping_number',
                                        blank=True, null=True)
    price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name='food_price')
    extra = models.BooleanField(default=False)

    def __str__(self):
        if self.size:
            return f"{self.name} {self.size} - {self.price}$"
        return f"{self.name} - {self.price}$"


class OrderNumber(models.Model):
    username = models.CharField(max_length=64, default='')
    email = models.CharField(max_length=64, default='')
    date = models.DateTimeField(auto_now_add=True)
    in_cart = models.BooleanField(default=True)
    in_process = models.BooleanField(default=True)
    done = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.id}: {self.username} on {self.date} in {self.total}"


class Order(models.Model):
    username = models.CharField(max_length=64, default='')
    food = models.ForeignKey(Food, related_name='order_food', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    order_num = models.ForeignKey(OrderNumber, on_delete=models.CASCADE, related_name="order_items")
    toppings = models.ManyToManyField(Topping, blank=True, related_name='pizza')
    extra = models.BooleanField(default=False)
    extra_sub = models.ManyToManyField(ExtraSub, blank=True, related_name='subs')

    def __str__(self):
        """
        String for representing the Model object.
         """
        return f"{self.food}"

