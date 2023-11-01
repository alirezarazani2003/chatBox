from django.urls import path
from . import views
urlpatterns = [
    path('',views.option,name = 'option'),
    path('login/',views.login,name = 'login'),
    path('register/',views.register , name = 'register'),
]