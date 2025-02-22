# Generated by Django 5.0.7 on 2024-07-29 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='attributes_ids',
            field=models.ManyToManyField(to='products.attribute'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='products_ids',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]
