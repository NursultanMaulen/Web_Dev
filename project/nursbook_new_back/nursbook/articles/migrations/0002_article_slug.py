# Generated by Django 4.2 on 2023-05-04 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.CharField(default='DEFAULT SLUG', max_length=255),
        ),
    ]