# Generated by Django 3.2.9 on 2021-12-05 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_alter_orders_typevesch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Email клиента'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='type',
            field=models.TextField(blank=True, help_text='тип вещей указынный клиентом', max_length=1000, null=True, verbose_name='Указан тип вещей'),
        ),
    ]
