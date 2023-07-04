from django.db import models
import datetime
from django.contrib.auth.models import User


# Create your models here.




# Doctor models

class Doctor1(User):
    CHOICES = [
        ("M", "Male"),
        ("F", "Female"),

    ]
    Doctor_Image = models.ImageField(upload_to='Doctor', verbose_name='Doctor Image')
    phone_number = models.IntegerField(default=0)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=6,  choices=CHOICES )
    biography = models.TextField(null=True)
    nationality = models.CharField(max_length=50, null=True)
    academic_degree = models.CharField(max_length=50, null=True)


    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

    def __str__(self):
        return self.username





# Patient model

class Patient(User):
    CHOICES = [
        ("M", "Male"),
        ("F", "Female"),

    ]
    patientimage = models.ImageField(upload_to='patient', verbose_name='patient_image')
    phone_number= models.IntegerField(default=0)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=100 , null=True)
    gender = models.CharField(max_length=6 , null=True , choices= CHOICES)
    biography = models.TextField(null=True)
    nationality = models.CharField(max_length=50, null=True)
    class Meta:
             verbose_name = "Patient"
             verbose_name_plural = "Patients"

    def __str__(self):
            return str(self.username)

# patien image


class Image(models.Model):
    image = models.ImageField(upload_to='cancer', verbose_name='patient_image' , null=True)
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return str(self.image)

class Treatment(models.Model):

            CHOICES = [
        ("children", "children"),
        ("teen", "teen"),
        ("adult", "adult"),
           ]


            tImage = models.ImageField(upload_to='treatment', verbose_name='Treatment Image')
            name = models.CharField(verbose_name='Treatment Name', max_length=50)
            dosage = models.IntegerField(verbose_name='Treatment Daily  Dosage ')
            Expiration_date = models.DateField(verbose_name='Treatment Expiration date')
            company= models.CharField(max_length=50, verbose_name='Company of product ')
            age_categories=models.CharField(max_length=20, choices=CHOICES, verbose_name='Age Categories')
            before_eating = models.BooleanField(default=True , verbose_name='Before Eating ')
            class Meta:
                verbose_name = "Treatment"
                verbose_name_plural = "Treatments"

            def __str__(self):
                return self.name
