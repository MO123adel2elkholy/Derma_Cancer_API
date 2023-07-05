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




from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


