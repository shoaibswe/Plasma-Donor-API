# Generated by Django 2.2.10 on 2020-06-10 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plasma_donor_lists', '0003_plasmadonorlist_gender'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PlasmaDonorList',
            new_name='A_PositiveDonorList',
        ),
    ]
