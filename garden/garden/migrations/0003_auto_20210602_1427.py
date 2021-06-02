# Generated by Django 3.2.4 on 2021-06-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0002_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='effort_level',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='experience_level',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='moniker',
            field=models.CharField(default="Allison's Aunt", max_length=240),
            preserve_default=False,
        ),
    ]