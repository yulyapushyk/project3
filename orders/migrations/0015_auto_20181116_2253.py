# Generated by Django 2.0.3 on 2018-11-16 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20181116_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='username',
            field=models.CharField(default='', max_length=64),
        ),
    ]
