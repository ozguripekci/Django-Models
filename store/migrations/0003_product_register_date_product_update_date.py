# Generated by Django 4.1 on 2022-08-18 20:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_options_product_about_product_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
