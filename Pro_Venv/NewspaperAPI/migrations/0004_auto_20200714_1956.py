# Generated by Django 3.0.8 on 2020-07-14 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewspaperAPI', '0003_auto_20200714_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspaper',
            name='description',
            field=models.TextField(max_length=20),
        ),
    ]
