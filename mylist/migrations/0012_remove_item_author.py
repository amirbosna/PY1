# Generated by Django 4.1.3 on 2022-11-14 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylist', '0011_item_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='author',
        ),
    ]