# Generated by Django 4.0.6 on 2022-11-05 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0023_alter_photo_collections'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
