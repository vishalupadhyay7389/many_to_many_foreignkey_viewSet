from django.shortcuts import render
from .models import Student , StudentSerializer
from rest_framework.viewsets import ViewSet
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response


# Create your views here.

class StudentDetailView(ViewSet):
    def list(self , request):
        stud = Student.objects.all()
        studserlizer = StudentSerializer(stud, many=True)
        return Response(studserlizer.data)
    
    def create(self , request):
        stud = StudentSerializer(data=request.data)
        if stud.is_valid():
            stud.save()
            return Response(stud.data , status=status.HTTP_201_CREATED)
        return Response(stud.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self , request , pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serlizer = StudentSerializer(student)
        return Response(serlizer.data)
    
    def partial_update(self , request , pk):
        try:
            stud = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serlizer = StudentSerializer(stud ,data=request.data , partial=True)
        if serlizer.is_valid():
            serlizer.save()
            return Response(serlizer.data , status=status.HTTP_201_CREATED)
        return Response(serlizer.errors , status=status.HTTP_404_NOT_FOUND)
    def destroy(self , request , pk):
        try:
            stud = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        stud.delete()
            
