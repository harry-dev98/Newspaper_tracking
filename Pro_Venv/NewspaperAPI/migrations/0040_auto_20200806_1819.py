# Generated by Django 3.0.8 on 2020-08-06 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewspaperAPI', '0039_auto_20200804_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daily_cart',
            name='ac_no',
        ),
        migrations.RemoveField(
            model_name='daily_cart',
            name='newspaper',
        ),
        migrations.RemoveField(
            model_name='newspaper_payment',
            name='newspaper',
        ),
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='newspaper',
        ),
        migrations.DeleteModel(
            name='Regi',
        ),
        migrations.AlterField(
            model_name='newspaper',
            name='language',
            field=models.CharField(choices=[('Spanish', 'Spanish'), ('English', 'English')], max_length=50),
        ),
        migrations.DeleteModel(
            name='Daily_Cart',
        ),
        migrations.DeleteModel(
            name='Newspaper_Payment',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]