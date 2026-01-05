from django.shortcuts import render
from requests import request
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status


class StudentApi(APIView):

    #GET
    def get(self, request, pk=None):
        if pk:
            stu = Student.objects.get(pk=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return Response(serializer.data)

    #POST
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    #FULL UPDATE
    def put(self, request, pk=None):
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    #PARTIAL UPDATE
    def patch(self, request, pk=None):
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    #DELETE
    def delete(self, request, pk=None):
        stu = Student.objects.get(pk=pk)
        stu.delete()
        return Response({"msg": "Deleted"})