from django.shortcuts import render
from .jason import  DoctorJason, Patienjason , Imagejason , Treatmentjason
from .models import Doctor1 , Patient , Image , Treatment
from rest_framework import viewsets , status
from requests import get
import numpy as np
from rest_framework.parsers import FormParser , MultiPartParser
import PIL.Image as Ig
import keras as k
import tensorflow as tf


model = k.models.load_model('model3.h5')
media = 'media'

# function for make prediction for Your image

def make_prediction(path):

    # get your image path
    img = Ig.open(path)
    # resize your image
    img_r = img.resize((128, 128))

    # check if your image in rgb format or not

    if len(np.array(img_r).shape)<4:
        rgb_img = Ig.new('RGB',img_r.size)
        rgb_img.paste(img_r)
    else:
        rgb_img=img_r

    # here we convert into numpy array and reshape

    rgb_img = np.array(rgb_img ,dtype=np.float64)
    rgb_img = rgb_img.reshape(-1, 128, 128, 1)

    # here we make prediction

    prediction=model.predict(rgb_img)

    out_put=int(np.argmax(prediction))

    if out_put == 0:
        out_put = 'benign'
    elif out_put == 1:
        out_put = 'malignant'
    else:
        out_put = 'error'
    print(out_put)
    return out_put

# Doctor API

class DoctorApi(viewsets.ModelViewSet):
    queryset = Doctor1.objects.all()
    serializer_class = DoctorJason



# Patient API
class PatienApi(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = Patienjason

# Cancer Image API

class Imageapi(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = Imagejason
    parser_classes = (FormParser, MultiPartParser)

#  Treatment API

class TreatmentApi(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = Treatmentjason

# how to get Data from external api for testing

def get_data(request):
    url = 'http://127.0.0.1:8000/Patientapi/'
    data = get(url).json()
    print(data)
    return render(request, 'show_data.html', {"data":data})


from rest_framework import generics, permissions
from rest_framework.response import Response



# API for your prediction

class predictapiAPI(generics.GenericAPIView):
    serializer_class = Imagejason
    queryset = Image.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image = request.data['image']
        im = Image()
        im.image = image
        im.save()
        out = make_prediction(image)
        cancer = str(serializer.save())
        json = {
            'data' : cancer,
            'message': out,
        }
        return Response(json, status=status.HTTP_400_BAD_REQUEST)



