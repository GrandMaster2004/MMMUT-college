# Generated by Django 3.2.13 on 2023-02-05 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0016_attn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attn',
            name='room_no',
        ),
    ]