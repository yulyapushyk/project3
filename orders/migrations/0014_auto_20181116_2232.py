# Generated by Django 2.0.3 on 2018-11-16 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20181116_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='toppings',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='order',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
