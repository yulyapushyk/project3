# Generated by Django 2.0.3 on 2018-11-08 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraCheese',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_cheese', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_category', to='orders.Category')),
                ('extra_cheese', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='subs_extra_cheese', to='orders.ExtraCheese')),
            ],
        ),
        migrations.CreateModel(
            name='PizzaType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ToppingNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='price',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='food_price', to='orders.Price'),
        ),
        migrations.AddField(
            model_name='food',
            name='select_toppings',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='pizza_topping_number', to='orders.ToppingNumber'),
        ),
        migrations.AddField(
            model_name='food',
            name='size',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='food_size', to='orders.Size'),
        ),
        migrations.AddField(
            model_name='food',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='pizza_topping', to='orders.Topping'),
        ),
        migrations.AddField(
            model_name='food',
            name='type',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='pizza_type', to='orders.PizzaType'),
        ),
    ]
