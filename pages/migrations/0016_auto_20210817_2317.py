# Generated by Django 3.1.1 on 2021-08-18 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_wgnasphotopage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wgnasphotocomment',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.wgnasphoto'),
        ),
    ]