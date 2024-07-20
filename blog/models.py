from django.db import models

# Create your models here.
#Los modelos es la informacion que se envia a la base de datos, vamos a crear un modelo post

class Post(models.Model):
    #Tenemos que darle los diferentes campos que qeueramos editar
    title = models.CharField(max_length = 250)
    content=models.TextField()
    
    #Podemos agregar el titulo al modelo 
    def __str__(self):
        return self.title