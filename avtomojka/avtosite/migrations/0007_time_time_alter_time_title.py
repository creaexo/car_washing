# Generated by Django 4.0.2 on 2022-06-12 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avtosite', '0006_time_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='time',
            name='time',
            field=models.CharField(default='', max_length=5, verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='time',
            name='title',
            field=models.CharField(max_length=13, verbose_name='День и время записи'),
        ),
    ]