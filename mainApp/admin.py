from django.contrib import admin
from .models import ToDo

# Register your models here.
#admin fill will create a interface of that fields you mentioned in modules

admin.site.register(ToDo)
