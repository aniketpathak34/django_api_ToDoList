from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.
#this all class is CRUD operations of API

class ListTodo(generics.ListAPIView):  #this class use to View the data
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class UpdateToDo(generics.RetrieveUpdateAPIView): #this class use to Update the data
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class CreateTodo(generics.CreateAPIView):   #this class use to Create the data
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DeleteTodo(generics.DestroyAPIView):  #this class use to Delete the data
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

