# Generated by Django 3.0.8 on 2020-07-15 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewspaperAPI', '0014_auto_20200715_0910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Create_date',
            new_name='add_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
    ]
