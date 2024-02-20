from django.db import models
from rest_framework import serializers

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    school = models.ForeignKey(School , on_delete=models.CASCADE , related_name='students')
    extra_activity = models.ManyToManyField('Activity' ,related_name='students')
    
    def __str__(self):
        return self.name
    
class Activity(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name
    

# class StudentSerlizer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    school_name = serializers.CharField(source='school.name', read_only=True)
    extra_activity_names = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'school', 'extra_activity', 'school_name', 'extra_activity_names']

    def get_extra_activity_names(self, obj):
        return [activity.name for activity in obj.extra_activity.all()]

    
    
    
