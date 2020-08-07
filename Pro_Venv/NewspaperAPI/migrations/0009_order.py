# Generated by Django 3.0.8 on 2020-07-14 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NewspaperAPI', '0008_auto_20200715_0338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewspaperAPI.Consumer')),
            ],
        ),
    ]
