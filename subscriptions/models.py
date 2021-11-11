from django.db import models
from django.urls import reverse

from django.contrib.contenttypes.fields import GenericRelation


class Orders(models.Model):
    name = models.CharField('Имя клиента', max_length=255)
    phone = models.CharField('Номер телефона клиента', max_length=255, null=True)
    email = models.CharField('Email клиента', max_length=255, null=True)
    prosmotr = models.BooleanField('Заявка просмотрена ', default=False, help_text='просмотрена ли заявка?')
    obrabotka = models.BooleanField('Заявка обработана ', default=False, help_text='обработана  ли заявка?')
    obrabotka_scklad = models.BooleanField('Уже на складе', default=False, help_text='Вещи по заявке на складе?')
    obrabotka_end = models.BooleanField('Заявка закрыта', default=False, help_text='Заявка обрабатона и в архиве?')
    created = models.DateTimeField('Дата создания заявки',auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.email



    class Meta:
        
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'
