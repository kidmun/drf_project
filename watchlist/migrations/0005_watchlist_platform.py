# Generated by Django 4.0.4 on 2022-05-27 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0004_remove_watchlist_platform'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='platform',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='watchlist.streamplatform'),
            preserve_default=False,
        ),
    ]
