# Generated by Django 2.0.3 on 2018-12-03 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0042_auto_20181201_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordernumber',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
