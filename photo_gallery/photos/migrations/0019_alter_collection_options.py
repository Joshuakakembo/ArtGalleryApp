# Generated by Django 4.0.6 on 2022-08-14 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0018_collection_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['name']},
        ),
    ]
