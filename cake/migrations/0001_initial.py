# Generated by Django 2.2.4 on 2020-01-10 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('text', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_cake', to=settings.AUTH_USER_MODEL)),
                ('photos', models.ManyToManyField(blank=True, default=None, to='photo.Photo')),
                ('updated_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_cake', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
