# Generated by Django 5.0.7 on 2024-08-06 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='search_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cities', models.CharField(max_length=255)),
                ('city_state', models.CharField(max_length=255)),
            ],
        ),
    ]
