from django.shortcuts import render , get_object_or_404
from .models import blog
# Create your views here.

def blogs(request):
    modblog = blog.objects.order_by('-date')


    return render(request , 'blog/blog.html' , {'models' : modblog})

def details(request, blog_id):
    blogg = get_object_or_404( blog ,pk=blog_id)
    return render(request , 'blog/details.html' , {'bloggg' : blogg})
