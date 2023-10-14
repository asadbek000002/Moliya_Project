from django.contrib import admin
from .models import Employee, Course, UserContract, About, Newslatter, PaymentCost


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'position', 'created', 'updated']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description', 'continuity', 'number_of_people', 'course_program', 'offer']


class PaymentCostInline(admin.TabularInline):
    model = PaymentCost
    raw_id_fields = ['contract']


@admin.register(UserContract)
class UserContractAdmin(admin.ModelAdmin):
    list_display = ['user', 'address']
    inlines = [PaymentCostInline]


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['image']
    


@admin.register(PaymentCost)
class PaymentCostAdmin(admin.ModelAdmin):
    list_display = ['price', 'created', 'contract']


@admin.register(Newslatter)
class NewslatterAdmin(admin.ModelAdmin):
    list_display = ['title', 'images', 'description', 'created', 'post_type', 'choose']