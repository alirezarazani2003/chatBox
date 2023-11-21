from django.contrib.auth import authenticate, login, logout
from . import models
from django.db import IntegrityError
from django.contrib import messages
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view 
from . import serializer
from rest_framework.authtoken.models import Token


# Create your views here.
@api_view(['POST','GET'])
def register(request:Request):
    if request.method == 'POST':
        print(request.data)
        serializerr = serializer.UserSerializer(data=request.data)
        try :
            if serializerr.is_valid():
                serializerr.save()
        except :
            return Response({"message": "Username already taken."},status.HTTP_200_OK)
    elif request.method == 'GET':
        ls = models.User.objects.all()
        user_serializer = serializer.UserSerializer(ls, many=True)
        return Response(user_serializer.data,status.HTTP_200_OK)
    return Response(None)

@api_view(['GET','POST'])
def login_view(request : Request):
    if request.method == "POST":
        # Attempt to sign user in
        # personalID = request.POST["personalID"]
        # password = request.POST["password"]
        personalID = request.data['personalID']
        password = request.data['password']
        user = authenticate(request, personalID=personalID, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return Response(True)

        else:
            return Response(None)
    if request.method =='GET':
        # ls = models.User.objects.all()
        # user_serializer = serializer.UserSerializer(ls, many=True)
        # return Response(user_serializer.data,status.HTTP_200_OK)
        return Response('nothing')
    return Response(None)
# def logout_view(request):
# #     logout(request)
#     pass
# #     #API

@api_view(['GET'])
def test(request : Request):
    ls = models.User.objects.all()
    user_serializer = serializer.UserSerializer(ls, many=True)
    return Response(user_serializer.data,status.HTTP_200_OK)