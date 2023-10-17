from django.shortcuts import render
from rest_framework import generics
from .serializers import EmployeeSerializer, CourseSerializer, AboutSerializer, \
NewslatterSerializer, ResultSerializer, UserContractOneSerializer, \
UserContractTwoSerializer, UserContractThreeSerializer

from .models import Employee, Course, About, Newslatter, Result, UserContract
from rest_framework.decorators import api_view


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


class UserContractOneList(generics.CreateAPIView):
    queryset = UserContract.objects.all()
    serializer_class = UserContractOneSerializer

    def perform_create(self, serializer):
        course = Course.objects.get(id=self.kwargs[self.lookup_field])
        serializer.save(course=course, user=self.request.user, step=1)
    

class UserContractTwoList(generics.UpdateAPIView):
    queryset = UserContract.objects.all()
    serializer_class = UserContractTwoSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user, step=2)


class UserContractThreeList(generics.UpdateAPIView):
    queryset = UserContract.objects.all()
    serializer_class = UserContractThreeSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user, step=3)

