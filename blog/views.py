from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,Category
from .forms import *
# Create your views here.


def Home(request):
    post= Post.objects.all()
    category = Category.objects.all()
    param = {'post':post, 'category':category}
    return render(request,'index.html',param)


def Categories(request,id):
    post=Post.objects.filter(category=id)
    category = Category.objects.all()
    param = {'post':post, 'category':category}
    
    return render(request,'index.html',param)


def DetailView(request,id):
    detail=Post.objects.get(id=id)
    category = Category.objects.all()
    cmnt=Comment.objects.filter( post=detail)
    print(cmnt)

    if request.method == "POST":
        form = CmntForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            user=request.POST.get("name","bhuban")
            print("comes here")
            user=User.objects.filter(email=user)
            if not user:
                result ="Please Login First"
                return(request, 'login.html',{'result':result})

            f.user=user[0]
            f.post = detail
            f.save()
            return redirect("detail", id=id)   
        else:
            print("no form")
    else:
        form =CmntForm()
    param={'detail':detail,'category':category,'form':form,'cmnt':cmnt}
    return render(request,'detail.html',param)


def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            return redirect('home')
        else:
            form = ContactForm(request.POST)
            category = Category.objects.all().order_by('category')
            return render(request, 'contact.html', {'form': form,'category':category})
    else:
        form = ContactForm()
    category = Category.objects.all()
    return render(request,'contact.html',{'form': form,'category':category})


def About(request):
    category = Category.objects.all()
    return render(request,'about.html',{'category':category})
