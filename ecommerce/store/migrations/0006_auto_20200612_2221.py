# Generated by Django 3.0.6 on 2020-06-12 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200612_2041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factura',
            old_name='razon_social',
            new_name='razon',
        ),
        migrations.RemoveField(
            model_name='order',
            name='bill',
        ),
        migrations.RemoveField(
            model_name='order',
            name='fact',
        ),
    ]
