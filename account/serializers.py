from .models import CustomUser
from rest_framework import serializers
from .services import validate_phone
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
# from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token
    def validate_password2(self, attrs):
        pasport = attrs.get('pasport_seria')
   
        if CustomUser.objects.filter(phone__iexact=pasport).exists():
            raise serializers.ValidationError(
                {'pasport': 'Pasport already exists'})
        return super().validate(attrs)


class RegisterSerializer(serializers.ModelSerializer):
    # phone = serializers.CharField(required=True, validators=[validate_phone])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('phone', 'password', 'password2', 'first_name')
        extra_kwargs = {
            'first_name': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    

    
    def create(self, validated_data):
        user = CustomUser.objects.create(
            phone=validated_data['phone'],
            first_name=validated_data['first_name'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

# class RegisterSerializer(serializers.Serializer):
#     phone = serializers.CharField(validators = [validate_phone])
#     password = serializers.CharField(write_only=True)]