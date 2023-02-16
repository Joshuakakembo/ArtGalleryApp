# Generated by Django 4.0.6 on 2022-07-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_alter_photo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='slug',
            field=models.SlugField(help_text='Enter a unique, descriptive URL path (e.g. based on the title) containing only lowercase letters, numbers,  and hyphens (instead of spaces). ', max_length=60, unique=True),
        ),
    ]
