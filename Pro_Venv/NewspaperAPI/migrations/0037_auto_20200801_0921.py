# Generated by Django 3.0.8 on 2020-08-01 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewspaperAPI', '0036_auto_20200731_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='newspaper',
        ),
        migrations.AddField(
            model_name='order',
            name='newspaper',
            field=models.ManyToManyField(to='NewspaperAPI.Newspaper'),
        ),
    ]
