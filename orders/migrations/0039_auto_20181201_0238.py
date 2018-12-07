# Generated by Django 2.0.3 on 2018-12-01 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0038_ordernumber_in_process'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='category',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='order',
            name='size',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='order',
            name='topping_number',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='order',
            name='food',
            field=models.CharField(default='', max_length=64),
        ),
    ]
