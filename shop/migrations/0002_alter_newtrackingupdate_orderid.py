# Generated by Django 4.0.6 on 2022-07-21 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newtrackingupdate',
            name='orderId',
            field=models.CharField(default='', max_length=20),
        ),
    ]