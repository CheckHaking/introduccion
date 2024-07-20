from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView
from .forms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

#Vista para ver todos los post
class BlogListView(View):
     
    def get(self, request, *args, **kwargs):
        post = Post.objects.all()
        context = {
            'posts': post
        }
        return render(request, 'blog_list.html', context )
#Vista para crear un post
class BlogCreateView(View):
    
    def get(self, request, *args, **kwargs):
        
        form = PostCreateForm()
        
        context = {
            'form': form
        }
        
        return render(request, 'blog_create.html', context)
    
    def post(self, request, *args, **kwargs):
        
        if request.method =="POST":
            
            form = PostCreateForm(request.POST)
            
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')
                
                p, created =  Post.objects.get_or_create(title=title,content=content) 
                
                p.save()          
                return redirect('blog:home')
        
        context = {   
        }
        return render(request, 'blog_create.html', context)
#Vista para ver el contenido de un Post 
class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        
        post=get_object_or_404(Post, pk = pk)
        context = {
            'post':post
        }
        return render(request, 'blog_detail.html', context )
#Vista para editar un Post
class BlogUpdateView(UpdateView):
    #primero le pasamos el modelo que vamos a editar 
    model = Post
    #Le pasamos los campos que queremos editar 
    fields=['title', 'content']
    #Le pasamos la vista que vamos a usar para editar
    template_name = 'blog_update.html'    
    #Cuando se actualice quiero que me redirija a la misma pagina de el post 
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs={'pk':pk})

    