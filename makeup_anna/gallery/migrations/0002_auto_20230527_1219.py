# Generated by Django 3.2.18 on 2023-05-27 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(default='Перманентный макияж', max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(help_text='Здесь можно загрузить картинку, объёмом не более 5Мб.', upload_to='gallery/', verbose_name='Изображение'),
        ),
    ]
