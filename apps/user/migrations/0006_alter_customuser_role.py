# Generated by Django 4.2.3 on 2023-08-07 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_goldenuser_regularuser_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('regular', 'regular'), ('golden', 'golden')], max_length=10),
        ),
    ]
