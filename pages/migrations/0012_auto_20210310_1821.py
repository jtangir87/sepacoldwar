# Generated by Django 3.1.1 on 2021-03-10 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20201006_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
