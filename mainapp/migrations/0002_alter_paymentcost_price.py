# Generated by Django 4.2.6 on 2023-10-13 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentcost',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
