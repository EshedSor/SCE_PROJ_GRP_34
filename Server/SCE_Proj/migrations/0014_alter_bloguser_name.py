# Generated by Django 3.2.9 on 2022-01-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCE_Proj', '0013_alter_bloguser_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
