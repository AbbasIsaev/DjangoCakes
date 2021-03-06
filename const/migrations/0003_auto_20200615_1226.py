# Generated by Django 3.0.2 on 2020-06-15 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('const', '0002_auto_20200110_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='const',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Название блока'),
        ),
        migrations.AlterField(
            model_name='const',
            name='params',
            field=models.TextField(default='{\n    "key1": "value1",\n    "key2": "value2",\n    "key3": "value3"\n}', verbose_name='JSON параметры'),
        ),
    ]
