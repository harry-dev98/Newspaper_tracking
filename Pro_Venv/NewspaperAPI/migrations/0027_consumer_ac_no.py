# Generated by Django 3.0.8 on 2020-07-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewspaperAPI', '0026_auto_20200727_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='ac_no',
            field=models.IntegerField(default=0),
        ),
    ]
