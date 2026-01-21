from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#there is also one readonlymodelviewset concept similar to this modelviewset
#which provides read-only operations (list and retrieve) for the model.
#all the things are same as above replace modelviewset with readonlymodelviewset