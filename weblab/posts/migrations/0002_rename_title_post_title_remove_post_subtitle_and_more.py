# Generated by Django 4.0 on 2021-12-26 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='Subtitle',
        ),
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
    ]
