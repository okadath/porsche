# Generated by Django 2.2.13 on 2020-07-07 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_auto_20200625_0624'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(default=None, max_length=149),
        ),
    ]
