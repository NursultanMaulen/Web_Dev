# Generated by Django 4.1.7 on 2023-04-12 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_vacancy'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.TextField(default='Lolek address', max_length=255),
        ),
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.CharField(default='Lolek city', max_length=255),
        ),
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(default='Lolek description', max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(default='Lolek', max_length=255),
        ),
    ]