# Generated by Django 4.2.3 on 2023-07-31 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productline',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]