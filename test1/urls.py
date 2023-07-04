from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import DoctorApi , PatienApi , Imageapi , TreatmentApi


router = routers.DefaultRouter()
router.register('Doctorapi', DoctorApi)
router.register('Patientapi', PatienApi)
router.register('Imageapi', Imageapi)
router.register('TreatmentApi', TreatmentApi)

# router.register('cancer_perdiction', cancer_perdiction)





urlpatterns = [
    path('', include(router.urls)),
    # path('c_p', cancer_perdiction, name='cancer_perdiction')

]
