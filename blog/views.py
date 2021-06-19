from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,Category
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def Home(request):
    obj= Post.objects.all().order_by('-order')
    category = Category.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(obj, 6)

    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        topics = paginator.page(1)
    except EmptyPage:
        topics = paginator.page(paginator.num_pages)

    param = {'topics': topics, 'category':category}
    return render(request,'index.html',param)


def Categories(request,id):
    obj=Post.objects.filter(category=id)
    category = Category.objects.all()
    

    page = request.GET.get('page', 1)
    paginator = Paginator(obj, 6)

    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        topics = paginator.page(1)
    except EmptyPage:
        topics = paginator.page(paginator.num_pages)

    param = {'topics': topics, 'category':category}
    
    return render(request,'index.html',param)


def DetailView(request,id):
    detail=Post.objects.get(id=id)
    print(detail)
    category = Category.objects.all()
    cmnt=Comment.objects.filter( post=detail)
    replies=[]
    for i in cmnt:
        print(i)
        rep=Reply.objects.filter(reply_to=i).exists()
        print(rep)
        if rep:
            rep=Reply.objects.filter(reply_to=i)
            replies.append(rep)
        
    print(replies)
    if request.method == "POST":
        form = CmntForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            user=request.POST.get("name","bhuban")
            user=User.objects.filter(email=user)
            if not user:
                result ="Please Login First"
                return(request, 'login.html',{'result':result})

            f.user=user[0]
            f.post = detail
            f.save()
            return redirect("detail", id=id)   
        
    else:
        form =CmntForm()
    param={'detail':detail,'category':category,'form':form,'cmnt':cmnt,'reply':replies}
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



def ReplyView(request,id):
    cmnt=Comment.objects.get(id=id)
    category = Category.objects.all()
    replies = Reply.objects.filter(reply_to=cmnt)
    print(replies)
    if request.method=="POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            user=request.POST.get("name","bhuban")
            user=User.objects.filter(email=user)
            if not user:
                result ="Please Login First"
                return(request, 'login.html',{'result':result})

            f.reply_by=user[0]
            f.reply_to =cmnt
            f.save()
            return redirect("reply", id=id) 

    else:
        form = ReplyForm()
        param={'category':category,'form':form,'cmnt':cmnt,'reply':replies}

    return render(request,"reply.html",param)



