# Generated by Django 3.1.7 on 2021-05-21 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210521_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='category',
        ),
    ]
