# Generated by Django 5.0.7 on 2024-07-29 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_cena'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='published_on',
            field=models.TextField(blank=True, null=True),
        ),
    ]
