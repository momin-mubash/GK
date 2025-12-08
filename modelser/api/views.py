from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
import io

@csrf_exempt
def student_api(request):
    #Read
    if request.method == 'GET':
        # Read ID from query params
        id = request.GET.get('id', None)

        # If ID is provided → return single student
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
            except Student.DoesNotExist:
                return JsonResponse({'error': 'Student not found'}, status=404)

            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data, safe=False)

        # If NO ID → return all students
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)

    
    #create
    if request.method == 'POST':#POST=Client → “Take my data and save it.”GET=Client → “Give me your data.”
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)    
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}        
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    #update
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        roll = pythondata.get('roll')
        stu = Student.objects.get(roll=roll)
        serializer = StudentSerializer(stu , data = pythondata , partial = True)#remove partial=true for complete update
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data , content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data , content_type='application/json')
    

    #Delete
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        roll = pythondata.get('roll')
        stu = Student.objects.get(roll = roll)
        stu.delete()
        res={'msg':f'Data Deleted of {roll}!!'}
        #json_data = JSONRenderer().render(res)
        #return HttpResponse(json_data , content_type='application/json')
        return JsonResponse(res,safe = False)
        
