# Generated by Django 3.2.19 on 2023-07-26 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_product_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='useradrres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('house', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('roadname', models.CharField(max_length=100)),
                ('landmark', models.CharField(max_length=100)),
                ('adrstype', models.CharField(max_length=100)),
                ('USER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
