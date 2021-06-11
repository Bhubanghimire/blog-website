from django.shortcuts import render

# Create your views here.
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from blog.forms import Creation

def Signup(request):
    if request.method == 'POST':
        print("bhuban123")
        form = Creation(request.POST)
        print(form.is_valid())
        
        if form.is_valid():
            print("abcd")
            print(form)
            user = form.save()
            return redirect('home')
        else:
            form = Creation(request.POST)
            return render(request, 'signup.html', {'form': form})
    else:
        form = Creation()
    return render(request, 'signup.html', {'form': form})