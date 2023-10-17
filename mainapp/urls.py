from django.urls import path
from .views import EmployeeList, CourseListAPIView, NewslatterList, BlogList, AboutListAPIView, ResultList, \
UserContractOneList, UserContractTwoList, UserContractThreeList

urlpatterns = [
    path('employee/', EmployeeList.as_view(), name='employee'),
    path('courses/', CourseListAPIView.as_view()),
    path('newslatter/', NewslatterList.as_view()),
    path('blog/', BlogList.as_view()),
    path('about/', AboutListAPIView.as_view()),
    path('result/', ResultList.as_view()),
    path('step/<pk>/', UserContractOneList.as_view()),
    path('steptwo/<pk>', UserContractTwoList.as_view()),
    path('stepthree/<pk>', UserContractThreeList.as_view()),

]
