# Generated by Django 4.0.6 on 2022-09-14 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0008_alter_account_account_number_alter_customer_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='interest_rate',
            field=models.PositiveIntegerField(default=15),
        ),
    ]
