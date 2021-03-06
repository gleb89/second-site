# Generated by Django 3.2.9 on 2021-12-05 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_user', models.CharField(max_length=255, verbose_name='Имя клиента')),
                ('message_text', models.TextField(help_text='сообщение от клиента', max_length=1000, null=True, verbose_name='сообщение от клиента')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефонный номер клиента')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Дата создания комментария')),
                ('prosmotr', models.BooleanField(default=False, help_text='просмотрена ли заявка?', verbose_name='Заявка просмотрена ')),
            ],
            options={
                'verbose_name': 'Хочу в команду',
                'verbose_name_plural': 'Хотят в команду',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_user', models.CharField(max_length=255, verbose_name='Имя клиента')),
                ('message_text', models.TextField(help_text='сообщение от клиента', max_length=1000, null=True, verbose_name='сообщение от клиента')),
                ('moderation', models.BooleanField(default=False, help_text='Комментарий допущен?', verbose_name='Комментарий допущен?')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Дата создания комментария')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='TypesItem',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Артикул вещи')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Тип вещи')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Вещь',
                'verbose_name_plural': 'Вещи',
            },
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя клиента')),
                ('phone', models.CharField(max_length=255, null=True, verbose_name='Номер телефона клиента')),
                ('email', models.CharField(max_length=255, null=True, verbose_name='Email клиента')),
                ('message', models.TextField(help_text='сообщение от клиента', max_length=1000, null=True, verbose_name='сообщение от клиента')),
                ('prosmotr', models.BooleanField(default=False, help_text='просмотрена ли заявка?', verbose_name='Заявка просмотрена ')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Дата создания заявки')),
            ],
            options={
                'verbose_name': 'Заявку на сотрудничество',
                'verbose_name_plural': 'Заявки на сотрудничество',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Артикул заявки')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Имя клиента')),
                ('phone', models.CharField(max_length=255, null=True, verbose_name='Номер телефона клиента')),
                ('email', models.CharField(max_length=255, null=True, verbose_name='Email клиента')),
                ('type', models.TextField(help_text='тип вещей указынный клиентом', max_length=1000, null=True, verbose_name='Указан тип вещей')),
                ('prosmotr', models.BooleanField(default=False, help_text='просмотрена ли заявка?', verbose_name='Заявка просмотрена ')),
                ('obrabotka', models.BooleanField(default=False, help_text='обработана  ли заявка?', verbose_name='Заявка обработана ')),
                ('obrabotka_scklad', models.BooleanField(default=False, help_text='Вещи по заявке на складе?', verbose_name='Уже на складе')),
                ('obrabotka_end', models.BooleanField(default=False, help_text='Заявка обрабатона и в архиве?', verbose_name='Заявка закрыта')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Дата создания заявки')),
                ('data_succes', models.DateTimeField(null=True, verbose_name='Дата когда нужно забрать вещи')),
                ('typevesch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions.typesitem', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Заявку',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
