from rest_framework import serializers
from .models import *


#this file helps to convert a complex python data to a jason data

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:

        model = ToDo
        fields = ('id','Title', 'Description', 'Date', 'Completed')

