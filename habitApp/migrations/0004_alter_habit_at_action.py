# Generated by Django 5.0.6 on 2024-06-17 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitApp', '0003_alter_habit_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='at_action',
            field=models.TimeField(default='09:00:00', help_text='укажите в какое время выполнять действие', verbose_name='Время действия'),
        ),
    ]
