# Generated by Django 3.2.13 on 2023-02-04 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0011_auto_20230204_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mess_schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel_name', models.CharField(max_length=30)),
                ('sunday', models.CharField(max_length=30)),
                ('monday', models.EmailField(max_length=30)),
                ('tuesday', models.CharField(max_length=100)),
                ('wednesday', models.CharField(max_length=50)),
                ('thursday', models.CharField(max_length=50)),
                ('friday', models.CharField(max_length=10)),
                ('sarturday', models.CharField(max_length=10)),
            ],
        ),
    ]
