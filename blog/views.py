from django.shortcuts import render

from . import models

def index(request):
    
    context = {
        'posts': models.Blog.objects.all()
    }
    
    return render(request, 'index.html', context)