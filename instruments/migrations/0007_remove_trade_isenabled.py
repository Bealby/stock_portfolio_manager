# Generated by Django 3.2.7 on 2021-10-04 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0006_remove_trade_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='isEnabled',
        ),
    ]
