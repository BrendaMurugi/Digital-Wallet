# Generated by Django 4.0.6 on 2022-09-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0006_alter_customer_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='employment_status',
            field=models.CharField(choices=[('Employed', 'Employed'), ('Self-employed', 'Self-employed'), ('Unemployed', 'Unemployed')], max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=15, null=True),
        ),
    ]
