from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'username or password is wrong')
            return redirect('/accounts/login')
    else:
        return render(request, 'accounts/login.html')

    

def logout(request):
    auth.logout(request)
    return render(request, 'accounts/login.html')