# Generated by Django 3.2.18 on 2023-05-28 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default='2022-02-22 22:22:22', help_text='Введите дату и время окончания акции\n        в формате 2022-02-22 22:22:22.', null=True, verbose_name='Дата и время окончания акции')),
            ],
            options={
                'verbose_name': 'Акция',
                'ordering': ['-date'],
            },
        ),
    ]
