# Generated by Django 5.1.2 on 2024-11-01 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parks',
            options={'verbose_name_plural': 'Parks'},
        ),
        migrations.AlterField(
            model_name='parks',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]