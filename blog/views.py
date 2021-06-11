from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def Home(request):
    post= Post.objects.all()
    param = {'post':post}
    for post in post:
        print(post.created_by.image)
    return render(request,'index.html',param)


def DetailView(request,id):
    detail=Post.objects.get(id=id)
    param={'detail':detail}
    return render(request,'detail.html',param)