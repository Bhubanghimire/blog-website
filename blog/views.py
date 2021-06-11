from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Category

# Create your views here.
def Home(request):
    post= Post.objects.all()
    category = []
    catg= Category.objects.order_by().values_list('category').distinct()
    for i in catg:
        for i in i:
            category.append(i)

    category=sorted(category)
    category = Category.objects.all().order_by()
    param = {'post':post, 'category':category}
    for post in post:
        print(post.created_by.image)
    return render(request,'index.html',param)


def Categories(request,id):
    post=Post.objects.filter(category=id)
    category = []
    catg=Category.objects.order_by().values_list('category').distinct()
    for i in catg:
        for i in i:
            category.append(i)

    category=sorted(category)
    category = Category.objects.all().order_by()
    param = {'post':post, 'category':category}
    for post in post:
        print(post.created_by.image)
    return render(request,'index.html',param)


def DetailView(request,id):
    detail=Post.objects.get(id=id)
    category = []
    catg=Category.objects.order_by().values_list('category').distinct()
    for i in catg:
        for i in i:
            category.append(i)

    category=sorted(category)
    category = Category.objects.all().order_by()
    param={'detail':detail,'category':category}
    return render(request,'detail.html',param)


def Contact(request):
    return render(request,'contact.html')

def About(request):
    return render(request,'about.html')
