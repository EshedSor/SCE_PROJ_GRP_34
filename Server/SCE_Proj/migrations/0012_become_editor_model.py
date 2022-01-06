# Generated by Django 3.2.9 on 2022-01-06 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SCE_Proj', '0011_alter_post_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='become_editor_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default=None, max_length=300)),
                ('requested_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='SCE_Proj.bloguser')),
            ],
            options={
                'db_table': 'become_editor_model',
            },
        ),
    ]