# Generated by Django 4.1.7 on 2023-05-30 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0005_image_patient_delete_student_image_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='patientimage',
            field=models.ImageField(default=0, upload_to='patient', verbose_name='patient_image'),
            preserve_default=False,
        ),
    ]
