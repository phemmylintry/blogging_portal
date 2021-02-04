from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication

from .serializers import CustomUserSerializer, UserLoginSerializer

from drf_yasg.utils import swagger_auto_schema

class UserCreateView(APIView):

    """j
    Creates a User
    """

    @swagger_auto_schema(
        request_body = CustomUserSerializer,
        operation_description = "Create a user" 
    )

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key

                return Response(json, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(ObtainAuthToken):

    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request' : request})

        if serializer.is_valid(raise_exception=True):

            return Response({
                "status" : "Sucess",
                "data" : serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)