# Generated by Django 2.2.4 on 2020-01-10 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('const', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='const',
            name='params',
            field=models.TextField(default='{\n    "key1": "value1",\n    "key2": "value2",\n    "key3": "value3"\n}'),
        ),
    ]
