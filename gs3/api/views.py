from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

# Create your views here.
def student_api(request):
    if request.method == 'GET':
     json_data = request.body
     stream = io.BytesIO(json_data)
     pythondata = JSONParser().parse(stream)
     id = pythondata.get('id' , None)
     if id is not None:
    #stu is a django model object(instance),its not a json not python dict
        stu = Student.objects.get(id = id)
    #Convert MODEL → JSON (using serializer)
        serializer = StudentSerializer(stu)#you get serializer object here
        json_data = JSONRenderer().render(serializer.data)#convert serializer object to json#serializer.data is the python dict
    #just above line creates json bytes from python dict
        return HttpResponse(json_data , content_type='application/json')
     
    
     stu = Student.objects.all()
     serializer = StudentSerializer(stu , many=True)
     json_data = JSONRenderer().render(serializer.data)#convert serializer object to json#serializer.data is the python dict
     return HttpResponse(json_data , content_type='application/json')