# Generated by Django 3.2.9 on 2021-11-29 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bloguser',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(default='', max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('nickname', models.CharField(default='', max_length=20, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('role', models.CharField(default='registered', max_length=10)),
            ],
            options={
                'db_table': 'bloguser',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField(max_length=100)),
                ('owner', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='SCE_Proj.bloguser')),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.DecimalField(decimal_places=1, max_digits=1)),
            ],
            options={
                'db_table': 'Rating',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('tags', models.CharField(default=None, max_length=250)),
                ('comments', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='SCE_Proj.comment')),
                ('owner', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='SCE_Proj.bloguser')),
                ('ratings', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SCE_Proj.rating')),
            ],
            options={
                'db_table': 'Post',
            },
        ),
        migrations.AddField(
            model_name='bloguser',
            name='comments',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SCE_Proj.comment'),
        ),
        migrations.AddField(
            model_name='bloguser',
            name='posts',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SCE_Proj.post'),
        ),
    ]
