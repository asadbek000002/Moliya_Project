from django.shortcuts import render
from rest_framework import generics
from .serializers import EmployeeSerializer, CourseSerializer, AboutSerializer, NewslatterSerializer, ResultSerializer
from .models import Employee, Course, About, Newslatter, Result



class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    
class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all() 
    serializer_class = CourseSerializer


class AboutListAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    
    
class NewslatterList(generics.ListAPIView):
    queryset = Newslatter.objects.filter(post_type=Newslatter.Status.NEWS)
    serializer_class = NewslatterSerializer

class BlogList(generics.ListAPIView):
    queryset = Newslatter.objects.filter(post_type=Newslatter.Status.BLOG)
    serializer_class = NewslatterSerializer
    
class ResultList(generics.ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer