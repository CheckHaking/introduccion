from django.contrib import admin

# Register your models here.

#Debemos registrar el modelo de Post que hemos creado 
from .models import Post

admin.site.register(Post)