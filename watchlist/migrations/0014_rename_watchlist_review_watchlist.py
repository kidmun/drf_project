# Generated by Django 4.0.4 on 2022-05-27 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0013_alter_watchlist_platform_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='WatchList',
            new_name='watchlist',
        ),
    ]
