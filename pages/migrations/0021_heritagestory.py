from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_auto_20220123_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeritageStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cover_image', models.ImageField(upload_to=pages.models.heritage_story_covers)),
                ('pdf_file', models.FileField(upload_to=pages.models.heritage_story_pdfs)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Heritage Story',
                'verbose_name_plural': 'Heritage Stories',
                'ordering': ['-created_at'],
            },
        ),
    ]
