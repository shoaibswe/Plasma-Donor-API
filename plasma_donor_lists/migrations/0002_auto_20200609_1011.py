# Generated by Django 2.2.10 on 2020-06-09 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plasma_donor_lists', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DonorList',
            new_name='PlasmaDonorList',
        ),
    ]
