# Generated by Django 3.0.5 on 2020-05-15 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0010_merge_20200515_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='id_trans',
        ),
    ]
