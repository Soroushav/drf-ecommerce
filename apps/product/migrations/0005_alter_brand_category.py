# Generated by Django 4.2.3 on 2023-07-31 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_brand_category_brand_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='category',
            field=models.ManyToManyField(to='product.category'),
        ),
    ]