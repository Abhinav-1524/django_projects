# Generated by Django 4.1.4 on 2023-01-25 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinebot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='Name',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='image_url',
            new_name='poster',
        ),
    ]
