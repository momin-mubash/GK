from django.http import JsonResponse
from django.shortcuts import render
from .models import student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


# model object - single student data

def student_detail(request,pk):
    stu = student.objects.get(id=pk) #model instance
    #print(stu)
    serializer = StudentSerializer(stu)# serialize model instance
    #print(serializer)
    #print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)#rendering into json
    #print(json_data)
    return HttpResponse(json_data, content_type='application/json')


# queryset - many student data
def student_list(request):
    stu = student.objects.all() #model instance
    #print(stu)
    serializer = StudentSerializer(stu , many=True)# serialize model instance
    #print(serializer)
    #print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)#rendering into json
    #print(json_data)
    return HttpResponse(json_data, content_type='application/json')