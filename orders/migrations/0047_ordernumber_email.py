# Generated by Django 2.0.3 on 2018-12-22 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0046_remove_order_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordernumber',
            name='email',
            field=models.CharField(default='', max_length=64),
        ),
    ]
