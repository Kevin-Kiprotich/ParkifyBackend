# Generated by Django 5.1.2 on 2024-11-01 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_parks_options_alter_parks_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='parks',
            name='booked',
            field=models.IntegerField(default=0),
        ),
    ]
