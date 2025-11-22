from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer

def student_api(request):
    if request.method == 'GET':
        # Read ID from query params (correct way for GET)
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

    return JsonResponse({'error': 'Invalid request method'}, status=400)
