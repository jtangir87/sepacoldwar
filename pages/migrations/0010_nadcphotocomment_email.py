# Generated by Django 3.1.1 on 2020-10-04 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_eventdescriptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='nadcphotocomment',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]