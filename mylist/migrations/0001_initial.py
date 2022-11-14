# Generated by Django 4.1.3 on 2022-11-09 00:56

import datetime
from django.db import migrations, models
from django.contrib.auth.models import User

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('name', models.CharField(max_length=200)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
