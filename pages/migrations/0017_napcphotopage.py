# Generated by Django 3.1.1 on 2021-08-19 23:05

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20210817_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='NAPCPhotoPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', tinymce.models.HTMLField(verbose_name='Page Text')),
            ],
            options={
                'verbose_name': 'NAPC Photo Page',
                'verbose_name_plural': 'NAPC Photo Page',
            },
        ),
    ]