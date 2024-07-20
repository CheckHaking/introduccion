from django.views.generic import View
from django.shortcuts import render

#Vamos a usar dos tipos de vistas, de classes y de funciones

class HomeView(View):
    #Dentro de la clase tenememos que llamar a la funcion get
    #Pide la informacion para que el usuario vea. en este caso el home view nos da acceso a estos dos metodos
    
    #args y kwargs: hace referencia a cualquier variable o cualquier parametro que el objeto del request pueda tener
    
    def get(self, request, *args, **kwargs):
        
        context = {
            
        }
        
        return render(request, 'index.html', context)
    
    
    #La funcion post se utiliza para que nosotros enviemos 
    def post():
        pass