from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView
from .views import MyObtainTokenPairView, RegisterView


urlpatterns = [
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='auth_register'),

]