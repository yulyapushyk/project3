# Generated by Django 2.0.3 on 2018-11-16 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20181117_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='toppings',
            field=models.ManyToManyField(blank=True, null=True, related_name='order_topping', to='orders.Topping'),
        ),
    ]
