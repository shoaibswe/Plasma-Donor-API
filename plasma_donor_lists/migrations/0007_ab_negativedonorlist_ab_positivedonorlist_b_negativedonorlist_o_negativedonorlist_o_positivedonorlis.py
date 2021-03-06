# Generated by Django 2.2.10 on 2020-06-11 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plasma_donor_lists', '0006_b_positivedonorlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='AB_NegativeDonorList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('blood_group', models.CharField(max_length=20)),
                ('last_date_of_blood_donation', models.DateField()),
                ('address', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('available', models.CharField(choices=[('available', 'available'), ('unavailable', 'unavailable')], max_length=15)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='AB_PositiveDonorList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('blood_group', models.CharField(max_length=20)),
                ('last_date_of_blood_donation', models.DateField()),
                ('address', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('available', models.CharField(choices=[('available', 'available'), ('unavailable', 'unavailable')], max_length=15)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='B_NegativeDonorList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('blood_group', models.CharField(max_length=20)),
                ('last_date_of_blood_donation', models.DateField()),
                ('address', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('available', models.CharField(choices=[('available', 'available'), ('unavailable', 'unavailable')], max_length=15)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='O_NegativeDonorList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('blood_group', models.CharField(max_length=20)),
                ('last_date_of_blood_donation', models.DateField()),
                ('address', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('available', models.CharField(choices=[('available', 'available'), ('unavailable', 'unavailable')], max_length=15)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='O_PositiveDonorList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('blood_group', models.CharField(max_length=20)),
                ('last_date_of_blood_donation', models.DateField()),
                ('address', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('available', models.CharField(choices=[('available', 'available'), ('unavailable', 'unavailable')], max_length=15)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=15)),
            ],
        ),
    ]
