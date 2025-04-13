from rest_framework import serializers
from users.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password

User=get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','email','phone_number','first_name','last_name')

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(required=True,write_only=True,validators=[validate_password])
    password2=serializers.CharField(required=True,write_only=True)

    class Meta:
        model=User
        fields= ['id','username','email','first_name','last_name','password','password2']

    def validate(self, attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError({"password":"password dont match"})
        return attrs
        
    def create(self,validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','phone_number','password']

    def update(self, instance, validated_data):
        password=validated_data.get('password',None)
        if password:
            validated_data['password']=make_password(password)
        return super().update(instance, validated_data)