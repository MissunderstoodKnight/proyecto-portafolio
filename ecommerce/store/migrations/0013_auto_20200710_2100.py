# Generated by Django 3.0.6 on 2020-07-11 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20200710_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordencompra',
            name='status',
            field=models.CharField(default='En espera', max_length=50),
        ),
    ]
