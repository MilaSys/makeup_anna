# Generated by Django 2.2.16 on 2023-06-30 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20230528_1554'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ['-created_at'], 'verbose_name': 'Обратная связь', 'verbose_name_plural': 'Обратная связь'},
        ),
    ]
