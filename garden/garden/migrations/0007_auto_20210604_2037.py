# Generated by Django 3.2.4 on 2021-06-04 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0006_profile_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='growingzone',
            name='name',
        ),
        migrations.AddField(
            model_name='growingzone',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='growingzone',
            name='subdivision',
            field=models.CharField(choices=[('A', 'a'), ('B', 'b')], default='A', max_length=1),
            preserve_default=False,
        ),
    ]
