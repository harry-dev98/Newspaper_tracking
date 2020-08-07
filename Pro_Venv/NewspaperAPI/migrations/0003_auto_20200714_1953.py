# Generated by Django 3.0.8 on 2020-07-14 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewspaperAPI', '0002_auto_20200714_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspaper',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newspaper',
            name='company',
            field=models.TextField(max_length=50),
        ),
    ]