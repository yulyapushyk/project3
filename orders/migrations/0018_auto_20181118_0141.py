# Generated by Django 2.0.3 on 2018-11-17 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_auto_20181117_0033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='toppings',
        ),
        migrations.AddField(
            model_name='food',
            name='toppings',
            field=models.CharField(default='None', max_length=64),
        ),
    ]
