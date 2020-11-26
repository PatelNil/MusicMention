# Generated by Django 3.1.1 on 2020-11-22 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_fav',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.CharField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.CharField(max_length=20),
        ),
    ]