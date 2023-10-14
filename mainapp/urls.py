from django.urls import path
from .views import EmployeeList, CourseListAPIView, NewslatterList, BlogList, AboutListAPIView

urlpatterns = [
    path('employee/', EmployeeList.as_view(), name='employee'),
    path('courses/', CourseListAPIView.as_view()),
    path('newslatter/', NewslatterList.as_view()),
    path('blog/', BlogList.as_view()),
    path('about/', AboutListAPIView.as_view()),
]
