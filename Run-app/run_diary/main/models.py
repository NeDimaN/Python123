from django.db import models


class Main(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True, verbose_name='Текст')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Функция'
        verbose_name_plural = 'Функции'


