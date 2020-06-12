# Generated by Django 2.2.10 on 2020-06-10 17:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('plasma_donor_lists', '0002_auto_20200609_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='plasmadonorlist',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
    ]