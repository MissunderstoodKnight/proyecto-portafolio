# Generated by Django 2.2.13 on 2020-06-29 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20200614_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_exp',
            field=models.DateField(blank=True, default=False, max_length=8, null=True),
        ),
    ]
