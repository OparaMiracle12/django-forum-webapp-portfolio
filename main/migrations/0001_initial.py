# Generated by Django 3.2 on 2021-05-07 20:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'forums',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ForumCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=40, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'forum categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('content', models.TextField(max_length=200)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('likes', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('dislikes', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.forum')),
            ],
            options={
                'verbose_name_plural': 'posts',
                'ordering': ['-date_updated', 'title'],
            },
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpeg', upload_to='posts')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.post')),
            ],
        ),
        migrations.AddField(
            model_name='forum',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.forumcategory'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='comments')),
                ('likes', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('dislikes', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='main.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.post')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]