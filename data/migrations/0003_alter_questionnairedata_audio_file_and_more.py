# Generated by Django 5.1.2 on 2025-01-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_alter_questionnairedata_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnairedata',
            name='audio_file',
            field=models.FileField(null=True, upload_to='Audio'),
        ),
        migrations.AlterField(
            model_name='questionnairedata',
            name='image_file',
            field=models.ImageField(null=True, upload_to='Images'),
        ),
        migrations.AlterField(
            model_name='questionnairedata',
            name='video_file',
            field=models.FileField(null=True, upload_to='Videos'),
        ),
    ]
