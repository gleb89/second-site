# Generated by Django 3.2.9 on 2021-12-08 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0015_alter_orders_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='created',
            field=models.DateTimeField(verbose_name='Дата создания заявки'),
        ),
    ]
