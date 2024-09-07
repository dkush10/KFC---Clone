from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        try:
            user=User.objects.get(username=username)
        except:
            return HttpResponse("Username does not exist!")
        if user.password==password:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Invalid username or password!")
        
    return render(request,'signin.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        User.objects.create(username=username,email=email,password=password)
        return redirect('signin')
    return render(request,'signup.html')

def logout_(request):
    logout(request)
    return redirect('signin')