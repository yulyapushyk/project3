# Generated by Django 2.0.3 on 2018-12-01 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0040_auto_20181201_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordernumber',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
