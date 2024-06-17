# Generated by Django 5.0.6 on 2024-06-17 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, help_text='Загрузите фото', null=True, upload_to='users/', verbose_name='Аватар'),
        ),
        migrations.AddField(
            model_name='user',
            name='chat_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ID чата'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, help_text='Введите город', max_length=20, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, help_text='Введите страну', max_length=20, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, help_text='Введите номер телефона', max_length=20, null=True, verbose_name='Телефон'),
        ),
    ]