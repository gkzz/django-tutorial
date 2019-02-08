from django.shortcuts import render
from .models import Blog #add

# Create your views here.
def index(request):      #add
    #return render(request, 'blogs/index.html')
    blogs = Blog.objects.order_by('-created_datetime')
    return render(request, 'blogs/index.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blogs/detail.html', {'blog': blog})