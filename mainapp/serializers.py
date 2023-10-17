from rest_framework import serializers
from .models import Employee, Course, About, Newslatter, Result, UserContract
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
        model = About
        fields = '__all__'
        
        
class NewslatterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newslatter
        fields = '__all__'
        

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class UserContractOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContract
        fields = ['id', 'course', 'first_name', 'passport', 'phone', 'address']
        extra_kwargs = {
            'id': {'read_only': True, 'required': False},
            'course': {'read_only': True, 'required': False},
        }


class UserContractTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContract
        fields = ['offerta_agreement',]


class UserContractThreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContract
        fields = ['paid', 'bolib_tolash', 'payment_image']


