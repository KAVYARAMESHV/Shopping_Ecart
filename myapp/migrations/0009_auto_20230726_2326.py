# Generated by Django 3.2.19 on 2023-07-26 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_bank_ordermain_ordersub'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermain',
            name='amount',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='ordermain',
            name='Status',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='ordermain',
            name='Total',
            field=models.CharField(default='', max_length=50),
        ),
    ]
