from django.db import models
from pytils.translit import slugify

from gallery.constants import MAX_LENGTH
from gallery.strings import MSG_LETTERS_RU, MSG_LETTERS_US


class Tag(models.Model):
    """
    Модель таблицы тэга.
    Attributes:
        name: CharField - название тэга
        slug: SlugField - кратное название латиницей
    """

    name = models.CharField(
        verbose_name='Тэг',
        max_length=MAX_LENGTH,
        unique=True,
        help_text=(
            'Введите название тэга.'
            f'{MSG_LETTERS_RU}'
        ),
    )
    slug = models.SlugField(
        verbose_name='Короткое название',
        max_length=MAX_LENGTH,
        unique=True,
        help_text=(
            'Укажите уникальный адрес тэга.'
            f'{MSG_LETTERS_US}'
        ),
    )

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['-id']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:MAX_LENGTH]
        super().save(*args, **kwargs)


class Gallery(models.Model):
    """
    Модель таблицы галлереи.
    Attributes:
        image: ImageField - фото работы
        tags: ForeignKey - ссылка (ID) на объект класса Tag
        pub_date: DateTimeField - дата создания
    """

    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='static/gallery/',
        blank=True,
        null=True,
        help_text='Здесь можно загрузить картинку, объёмом не более 5Мб.',
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тег',
        related_name='gallery',
        help_text='Введите id ассоциирующегося тега.',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата загрузки изображения',
        auto_now_add=True,
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return self.image
