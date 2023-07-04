from .models import  Doctor1, Patient , Image , Treatment
from rest_framework import serializers


# Doctor  serializer

class DoctorJason(serializers.ModelSerializer):
    class Meta:
       model = Doctor1
       fields = ('id', 'username', 'email', 'phone_number', 'nationality', 'age',  'address',
                 'biography', 'gender', 'academic_degree', "Doctor_Image")




# Patient serializer

class Patienjason(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'username', 'email', 'password', 'phone_number', 'nationality', 'age', 'patientimage',  'address','biography', 'gender')

# Cancer Image serializer

class Imagejason(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


#Treatment  serializer


class Treatmentjason(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = '__all__'




