from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model


User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, min_length=8)
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'username', 'posts', 'comments')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)
    token = serializers.CharField(read_only=True, allow_blank=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'token')

    def validate(self, attrs):
        email = attrs.get('email', None)
        password = attrs.get('password', None)

        #check if email or password was populated
        if not email and not password:
            raise serializers.ValidationError("Please enter email address")
        
        user = authenticate(email=email, password=password)

        #check is user exists
        if not user:    
            raise serializers.ValidationError("Invalid credentials")

        #check if user is acive
        if user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            attrs['token'] = token
        else:
            raise serializers.ValidationError("User not active, Please contact admin")

        return attrs
            

