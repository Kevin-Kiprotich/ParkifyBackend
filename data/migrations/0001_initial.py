# Generated by Django 5.1.2 on 2025-01-09 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionnaireData',
            fields=[
                ('id', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('formTitle', models.CharField(max_length=40)),
                ('formStatus', models.CharField(default='submitted', max_length=40)),
                ('datetime', models.CharField(max_length=200)),
                ('questions', models.TextField()),
                ('geometry_type', models.CharField(max_length=40, null=True)),
                ('image_file', models.ImageField(null=True, upload_to='media/Images')),
                ('audio_file', models.FileField(null=True, upload_to='media/Audio')),
                ('video_file', models.FileField(null=True, upload_to='media/Videos')),
            ],
            options={
                'verbose_name_plural': 'Reported Crimes',
            },
        ),
    ]