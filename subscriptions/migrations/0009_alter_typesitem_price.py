# Generated by Django 3.2.9 on 2021-12-05 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0008_alter_orders_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typesitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='Цена'),
        ),
    ]
