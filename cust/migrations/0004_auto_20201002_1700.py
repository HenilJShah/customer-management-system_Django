# Generated by Django 3.1.1 on 2020-10-02 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cust', '0003_auto_20201002_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('out of delivery', 'out of delivery'), ('delivery', 'delivery')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_Name', models.CharField(max_length=200, null=True)),
                ('prod_price', models.FloatField(max_length=50, null=True)),
                ('prod_category', models.CharField(choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')], max_length=200, null=True)),
                ('prod_desc', models.CharField(max_length=200, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='logs',
            new_name='date_create',
        ),
    ]