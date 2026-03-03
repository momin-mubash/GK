from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView

# Create your views here.
class StudentList(ListAPIView):
    # queryset = Student.objects.filter(passby='user1')
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby=user)#shows only user's own data
    
#prefer notes for two more filtering concepts:queryparameters ,DjangoFilterBackend

