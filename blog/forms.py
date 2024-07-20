from django import forms
#Vamos a traer el modelo que queremos manipular
from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        #Adentro de meta declaramos el modelo que queremos editar
        model = Post
        fields = ('title', 'content')