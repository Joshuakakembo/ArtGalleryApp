# Generated by Django 4.0.6 on 2022-08-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0017_collection_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
