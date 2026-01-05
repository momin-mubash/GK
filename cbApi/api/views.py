from django.shortcuts import render
from requests import request
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status


class StudentApi(APIView):
    def get(self, request, pk=None, format=None):
        # if pk is provided -> single student
        
        if pk is not None:
            try:
                stu = Student.objects.get(pk=pk)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            except Student.DoesNotExist:
                return Response({"error": "Student not found"}, status=404)

        # if pk not provided -> all students
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    

#create operation
   
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# COMPLETE UPDATE
def put(self, request, pk, format=None):
    try:
        stu = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=404)

    serializer = StudentSerializer(stu, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Complete Data Updated'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# PARTIAL UPDATE
def patch(self, request, pk, format=None):
    try:
        stu = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=404)

    serializer = StudentSerializer(stu, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# DELETE
def delete(self, request, pk, format=None):
    try:
        stu = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=404)

    stu.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
