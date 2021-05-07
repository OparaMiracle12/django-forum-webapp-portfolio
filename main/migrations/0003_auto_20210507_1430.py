# Generated by Django 3.2 on 2021-05-07 21:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210507_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='dislikes',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='dislikes',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
