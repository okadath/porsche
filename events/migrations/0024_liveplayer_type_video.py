# Generated by Django 2.2.13 on 2020-07-08 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0023_auto_20200708_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='liveplayer',
            name='type_video',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Live'), (2, 'SimulatedLive'), (3, 'VideoPlaceholder')], default=1),
        ),
    ]
