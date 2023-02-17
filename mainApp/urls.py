from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', UpdateToDo.as_view()),
    path('', ListTodo.as_view()),
    path('create/', CreateTodo.as_view()),
    path('delete/<int:pk>/', DeleteTodo.as_view()),
]


#all URLS are here to access the given CRUD operations