from rest_framework import serializers
from .models import Employee, Course, About, Newslatter
from .views import*


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course 
        fields = "__all__" 
        
        
class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        modul = About
        fields = '__all__'
        
        
class NewslatterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newslatter
        fields = '__all__'