# Generated by Django 4.1.3 on 2022-11-13 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylist', '0009_item_userid_alter_item_public'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='UserID',
            new_name='useridnummer',
        ),
    ]
