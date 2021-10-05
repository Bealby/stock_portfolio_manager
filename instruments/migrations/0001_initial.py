# Generated by Django 3.2.7 on 2021-10-04 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=254)),
                ('name', models.CharField(max_length=254)),
                ('iexId', models.CharField(max_length=254)),
                ('description', models.CharField(max_length=254)),
                ('holding_value', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('total_profit_loss', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('volume', models.DecimalField(decimal_places=0, default=0, max_digits=20)),
                ('buy_value', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('sell_value', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('profit_loss', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
            ],
        ),
    ]
