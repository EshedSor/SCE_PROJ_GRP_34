# Generated by Django 3.2.9 on 2021-11-29 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SCE_Proj', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloguser',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='bloguser',
            name='posts',
        ),
    ]