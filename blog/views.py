from django.http import HttpResponse
from .models import Post

def index(request):
    all_posts=Post.objects.all()
    html = ''
    for post in all_posts:
        url =str(post.id) + '/'
        html+='<a href="'+ url+ '">'+post.title+'</a><br>'
    return HttpResponse(html)


def detail(request,post_id):
    return HttpResponse("<h1>Post no :"+str(post_id)+"</h1>")
