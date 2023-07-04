# Generated by Django 4.2.1 on 2023-06-23 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0007_doctor1_academic_degree_doctor1_address_doctor1_age_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Treatment_name')),
                ('dosage', models.IntegerField(verbose_name='Treatment Dosage ')),
                ('Expiration_date', models.DateField(verbose_name='Treatment Expiration date')),
                ('company', models.CharField(max_length=50, verbose_name='Company of product ')),
                ('cancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test1.image', verbose_name='Cancer')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test1.patient', verbose_name='Patient')),
            ],
            options={
                'verbose_name': 'Treatment',
                'verbose_name_plural': 'Treatments',
            },
        ),
    ]
