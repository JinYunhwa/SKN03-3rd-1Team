# Generated by Django 5.1.1 on 2024-09-23 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_coupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='is_downloaded',
        ),
    ]