from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Order


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
#
#
# class PizzaForm(ModelForm):
#     class Meta:
#         model = Order()
#         fields = ['toppings']
#         widgets = {'toppings': forms.CheckboxSelectMultiple}


class PizzaForm(forms.Form):
    TOPPINGS = (
        ('PEPPERONI', 'pepperoni'),
        ('SAUSAGE', 'sausage'),
        ('MUSHROOMS', 'mushrooms'),
        ('ONIONS', 'onions'),
        ('HAM', 'ham'),
        ('CANADIAN BACON', 'canadian bacon'),
        ('PINEAPPLE', 'pineapple'),
        ('EGGPLANT', 'egglplant'),
        ('TOMATO & BASIL', 'tomato & basil'),
        ('GREEN PEPPERS', 'green peppers'),
        ('HAMBURGER', 'hamburger'),
        ('SPINACH', 'spinach'),
        ('ARTICHOKE', 'artichoke'),
        ('BUFFALO CHICKEN', 'buffalo chicken'),
        ('BARBECUE CHICKEN', 'barbecue chicken'),
        ('ANCHOVIES', 'anchovies'),
        ('BLACK OLIVES', 'black olives'),
        ('FRESH GARLIC', 'fresh garlic'),
        ('ZUCCHINI', 'zucchini'),
    )
    toppings = forms.MultipleChoiceField(choices=TOPPINGS, widget=forms.CheckboxSelectMultiple())