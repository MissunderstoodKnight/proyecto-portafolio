# Generated by Django 3.0.6 on 2020-06-14 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20200614_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordencompra',
            name='detalle',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
