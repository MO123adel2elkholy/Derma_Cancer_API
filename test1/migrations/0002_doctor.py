# Generated by Django 4.2.1 on 2023-05-14 22:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=10)),
                ('lname', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=10)),
                ('joindate', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctors',
            },
        ),
    ]
