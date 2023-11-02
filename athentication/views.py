from django.contrib.auth import authenticate, login, logout
from . import models
from django.db import IntegrityError
from django.contrib import messages

# Create your views here.

def register(request):
#     if request.method == "POST":
#         personalID = request.POST["personalID"]
#         workshop = request.POST["workshop"]
#         email = request.POST["email"]
#         role = request.POST["role"]
#         if username == "" or email =="":
            pass
#         #    return render (request, "auctions/register.html", {"message": "Invalid username or email",})
#         #API
            
            
#         # Ensure password matches confirmation
#         password = request.POST["password"]
#         confirmation = request.POST["confirmation"]
#         if password == "" or confirmation =="":
#         #    return render (request, "auctions/register.html", {"message": "password should be exist!",})
#             pass
        
#         if password != confirmation:
#             # return render(request, "auctions/register.html", {
#             #     "message": "Passwords must match."
#             # })
#             # API
#             pass

#         # Attempt to create new user
#         try:
#             user = models.User.objects.create_user(personalID,email, password,role,workshop)
#             user.save()
#         except IntegrityError:
#             # return render(request, "auctions/register.html", {
#             #     "message": "Username already taken."
#             # })
#             pass
#             #API
#         login(request, user)
#         return HttpResponseRedirect(reverse("index"))
#     else:
#         # return render(request, "auctions/register.html")
#         pass
#         #API
    


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
