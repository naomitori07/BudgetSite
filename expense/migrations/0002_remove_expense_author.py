# Generated by Django 2.0.8 on 2018-08-08 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='author',
        ),
    ]
