# Generated by Django 4.1.4 on 2022-12-18 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_shipment_origin'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
