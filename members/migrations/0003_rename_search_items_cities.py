# Generated by Django 5.0.7 on 2024-08-07 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_search_items_delete_cities'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='search_items',
            new_name='Cities',
        ),
    ]
