# Generated by Django 4.1.4 on 2023-01-27 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0004_remove_bill_cash'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='cash',
            field=models.IntegerField(null=True),
        ),
    ]