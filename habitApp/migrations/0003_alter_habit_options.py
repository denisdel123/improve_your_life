# Generated by Django 5.0.6 on 2024-06-15 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habitApp', '0002_alter_habit_action_alter_habit_associated_habit_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habit',
            options={'verbose_name': 'Привычка', 'verbose_name_plural': 'Привычки'},
        ),
    ]
