from django.contrib.auth import get_user_model
from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html

User = get_user_model()


class Adverisments(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название"
    )

    description = models.TextField(
        verbose_name="Описание"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена"
    )

    auction = models.BooleanField(
        default=False,
        verbose_name="Торг"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='module_4/')

    @admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html('<span>Сегодня в {}</span>', created_time)
        return self.created_at.strftime("%d.%m.%y в %H:%M:%S")

    @admin.display(description='дата обновления')
    def update_date(self):
        if self.updated_at.date() == timezone.now().date():
            update_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html('<span style= color:green> Сегодня в {}</span>', update_time)
        return self.created_at.strftime("%d.%m.%y в %H:%M:%S")

    @admin.display(description='изображение')
    def photo(self):
        if self.image:
            return format_html('<img src = "{}"/, height=100, width=200>', self.image.url)
        return format_html('<span>Нет фото</span>')

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'

    class Meta:
        db_table = "advertisements"
