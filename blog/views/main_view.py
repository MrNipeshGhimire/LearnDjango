from django.shortcuts import render,redirect
from ..models import Blog

def home(request):
    return render(request,'main/home.html')

def create_blog(request):

    if request.method == "POST":
        title = request.POST.get("title")
        subtitle = request.POST.get("subtitle")
        description = request.POST.get("description")
        blog = Blog(title=title,subtitle=subtitle,description=description)
        blog.save()
        return redirect("home")

    return render(request,'main/create_blog.html')

def single_blog(request):
    return render(request,'main/single_blog.html')

def edit_blog(request):
    return render(request,'main/edit_blog.html')