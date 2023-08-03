from django.db import models


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

    class Meta: 
        db_table = 'advertisements'

    # Актуальность объявления
    # Количество товара
    # Имя продавца + контакты
    # Возможен ли обмен
    # Адрес продажи/осмотре
    # Б/у товар или нет
    # Возможно ли взять в долг/рассрочку