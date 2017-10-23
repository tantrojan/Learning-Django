from django.shortcuts import render
from .models import Post

def index(request):
    posts=Post.objects.all()
    return render(request,"blog\index.html", {'posts':posts})


def detail(request,post_id):
    return HttpResponse("<h1>Post no :"+str(post_id)+"</h1>")
