# Generated by Django 5.0.7 on 2024-08-08 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_delete_cities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=1000, null=True),
        ),
    ]
