# Generated by Django 2.0.3 on 2018-11-15 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20181109_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='extra_cheese',
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Food'),
        ),
        migrations.DeleteModel(
            name='ExtraCheese',
        ),
    ]
