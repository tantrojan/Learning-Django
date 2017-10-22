from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is a blog page</h1>")

def detail(request,post_id):
    return HttpResponse("<h1>Post no :"+str(post_id)+"</h1>")
