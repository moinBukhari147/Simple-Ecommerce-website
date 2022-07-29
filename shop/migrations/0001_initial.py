# Generated by Django 4.0.6 on 2022-07-20 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('contactor_id', models.AutoField(primary_key=True, serialize=False)),
                ('contactor_name', models.CharField(max_length=50)),
                ('contactor_email', models.CharField(max_length=70)),
                ('contactor_phone', models.CharField(max_length=12)),
                ('contactor_query', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='newOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_jason', models.CharField(default='', max_length=500)),
                ('chekout_fname', models.CharField(default='', max_length=200)),
                ('chekout_lname', models.CharField(default='', max_length=200)),
                ('chekout_email', models.CharField(default='', max_length=50)),
                ('chekout_phone', models.CharField(default='', max_length=12)),
                ('chekout_address', models.CharField(default='', max_length=300)),
                ('chekout_city', models.CharField(default='', max_length=200)),
                ('chekout_zip', models.CharField(default='', max_length=200)),
                ('chekout_state', models.CharField(default='', max_length=200)),
                ('trackId', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='newTrackingUpdate',
            fields=[
                ('track_id', models.AutoField(primary_key=True, serialize=False)),
                ('orderId', models.IntegerField(default='')),
                ('orderUpdate', models.CharField(default='none', max_length=30)),
                ('timeUpdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=70)),
                ('product_desc', models.CharField(max_length=300)),
                ('product_price', models.IntegerField(default=0)),
                ('product_category', models.CharField(default='', max_length=50)),
                ('product_subcatrgory', models.CharField(default='', max_length=50)),
                ('pub_date', models.DateField()),
                ('product_image', models.ImageField(default='', upload_to='shop/pro_images')),
            ],
        ),
    ]