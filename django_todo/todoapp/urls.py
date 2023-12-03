from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('login', LoginView, name="login"),
    path('register', UserRegisterView, name='register'),
    path('', Home, name="home"),
    path('detail/<str:pk>', TaskDetail, name="detail"),
    path('addtask', AddTask, name="addtask"),
    path('edittask/<str:pk>', EditTask, name="edittask"),

    


]
