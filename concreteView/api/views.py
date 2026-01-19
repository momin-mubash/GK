from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

class StudentListCreate(ListAPIView,CreateAPIView):#ListCreateAPIView can also be used here
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDelete(RetrieveAPIView,UpdateAPIView,DestroyAPIView):#RetrieveUpdateDestroyAPIView can also be used here
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

