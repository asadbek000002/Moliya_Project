from django.contrib import admin
from .models import Employee, Course, UserContract, About


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'position', 'created', 'updated']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description', 'continuity', 'number_of_people', 'course_program', 'offer']


@admin.register(UserContract)
class UserContractAdmin(admin.ModelAdmin):
    list_display = ['user', 'address']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['image']