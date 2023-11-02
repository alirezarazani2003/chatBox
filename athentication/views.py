from django.contrib.auth import authenticate, login, logout
from . import models
from django.db import IntegrityError
from django.contrib import messages
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from . import serializer

# Create your views here.
@api_view(['POST','GET'])
def register(request:Request):
    if request.method == "POST":
        personalID = request.POST["personalID"]
        workshop = request.POST["workshop"]
        email = request.POST["email"]
        role = request.POST["role"]
        if username == "" or email =="":
            return Response({"message": "Invalid username or email"},status.HTTP_200_OK)
        pass
#         #API
            
            
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password == "" or confirmation =="":
            return Response({"message": "password should be exist!"},status.HTTP_200_OK)
        
        if password != confirmation:
            return Response({"message": "Passwords must match."})
            # API

        # Attempt to create new user
        try:
            user = models.User.objects.create_user(personalID,email, password,role,workshop)
            user.save()
        except IntegrityError:
            return Response({"message": "Username already taken."},status.HTTP_200_OK)
            #API
        login(request, user)
    else:
        return Response({"message": "Username already taken."},status.HTTP_200_OK)
        #API
    


def login_view(request):
#     if request.method == "POST":

#         # Attempt to sign user in
#         personalID = request.POST["personalID"]
#         password = request.POST["password"]
#         user = authenticate(request, personalID=personalID, password=password)

#         # Check if authentication successful
#         if user is not None:
#             # login(request, user)
            pass
            
#             # return HttpResponseRedirect(reverse("index"))
#         else:
#             # return render(request, "auctions/login.html", {
#             #     "message": "Invalid username and/or password."
#             # })
#             pass
#             #API
#     else:
#         # return render(request, "auctions/login.html")
#         #API
#         pass
    
def logout_view(request):
#     logout(request)
    pass
#     #API

@api_view(['GET'])
def test(request : Request):
    ls = models.User.objects.all()
    user_serializer = serializer.UserSerializer(ls, many=True)
    return Response(user_serializer.data,status.HTTP_200_OK)