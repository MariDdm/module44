from django.db import models
from django.contrib import admin
from django.utils.html import format_html


class Advertisement(models.Model):

    # Товар
    # строковое поле небольших размеров
    # "заголовок" - verbose_name - название поле извне
    title = models.CharField('заголовок', max_length =128)

    # Описание товара
    # Большое текстовое поле, для больших текстов
    description = models.TextField('описание')

    # Цена
    # Специальный тип данных с фиксированной точкой 
    price = models.DecimalField('цена', max_digits=10, decimal_places=2 )
    
    # Дата публикации
    # Поле записывается при создании объявления
    created_at = models.DateTimeField(auto_now_add=True)

    # Дата изменения/обновления
    # Поле записывается при каждом обновлении
    updated_at = models.DateTimeField(auto_now=True)

    # Уместен ли торг
    # Логический тип, два значения - правда или ложь
    auction = models.BooleanField('торг',  help_text = 'Отметьте, уместен ли торг')

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_date = self.created_at.strftime("%H:%M:%S")
            return format_html('<span style = "color:pink; font-weight:bold;">Сегодня в {} </span>', created_date)
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Дата редактирования')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_date = self.updated_at.strftime("%H:%M:%S")
            return format_html('<span style = "color:pink; font-weight:bold;">Сегодня в {} </span>', updated_date)
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")


    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"
    
    
    class Meta: 
        db_table = 'advertisements'

    # Актуальность объявления
    # Количество товара
    # Имя продавца + контакты
    # Возможен ли обмен
    # Адрес продажи/осмотре
    # Б/у товар или нет
    # Возможно ли взять в долг/рассрочку