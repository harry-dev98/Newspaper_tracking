# Generated by Django 3.0.8 on 2020-07-16 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewspaperAPI', '0021_auto_20200716_0756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newspaper',
            old_name='re_price',
            new_name='sa_price',
        ),
        migrations.RenameField(
            model_name='newspaper',
            old_name='sale_price',
            new_name='wh_price',
        ),
    ]
