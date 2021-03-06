# Generated by Django 4.0.2 on 2022-02-16 18:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CUSTOMER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=50)),
                ('nid', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('member_level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CUSTOMER_VISIT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_bill', models.IntegerField()),
                ('due_bill', models.IntegerField()),
                ('check_in', models.DateTimeField(default=datetime.datetime(2022, 2, 16, 18, 36, 44, 131968))),
                ('check_out', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reception.customer')),
            ],
        ),
        migrations.CreateModel(
            name='ROOM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField()),
                ('fare', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('type', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('availability', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OTHER_BOARDER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=30)),
                ('customer_visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reception.customer_visit')),
            ],
        ),
        migrations.CreateModel(
            name='INVOICE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_bill', models.IntegerField()),
                ('customer_visit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reception.customer_visit')),
            ],
        ),
        migrations.AddField(
            model_name='customer_visit',
            name='room_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reception.room'),
        ),
    ]
