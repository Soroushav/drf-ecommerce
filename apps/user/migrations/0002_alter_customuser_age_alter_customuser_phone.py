# Generated by Django 4.2.3 on 2023-07-24 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.PositiveIntegerField(null=True),
        ),
    ]