from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Read Operation
@api_view(['GET' , 'POST' , 'PUT' , 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request):
    if request.method == 'GET':
        roll = request.GET.get('roll')
        
        # If roll is provided → return single student
        if roll is not None:
            try:
                stu = Student.objects.get(roll=roll)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            except Student.DoesNotExist:
                return Response({"error": "Student not found"}, status=404)
        
        # If no roll → return all
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

#Create Operation
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Created'})
        return Response(serializer.errors)
    
#Update Operation
    if request.method=='PUT':
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu , data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
    

#Delete Operation
    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
    return Response({'msg':'student doesnt exist'})

    
