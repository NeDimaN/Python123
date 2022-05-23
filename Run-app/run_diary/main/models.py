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


# class Active(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Название')
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
#     content = models.TextField(blank=True, verbose_name='Контент')
#     km = models.IntegerField(blank=True, verbose_name='Расстояние')
#     time = models.TimeField(blank=True, verbose_name='Затраченное время')
#     min_pulse = models.ImageField(blank=True, max_length=4, verbose_name='Минимальный пульс')
#     av_pulse = models.ImageField(blank=True, max_length=4, verbose_name='Средний пульс')
#     max_pulse = models.ImageField(blank=True, max_length=4, verbose_name='Максимальный пульс')
#     photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
#     time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
#     time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
#     is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
#     cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
#
#     def __str__(self):
#         return self.title
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
#     slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
