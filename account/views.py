from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import Http404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import UserSerializer, UserUpdateSerializer, UserDataSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication



class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()

            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
                'token': token.key,
                'mobile':user.mobile,
                'first_name':user.first_name,
                'last_name':user.last_name,
                'birthday':user.birthday,
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserUpdateView(RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserUpdateSerializer

    def get_object(self):
        return self.request.user
           

class ChangePasswordView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        form=PasswordChangeForm(user=request.user, data=request.data)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return Response({'message':'The password has been succesfully changed!'}, status=status.HTTP_200_OK)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)



class GetUserDataVIew(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        serializer = UserDataSerializer(instance=request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
