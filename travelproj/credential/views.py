from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid")

    return render(request,'login.html')
def demo3(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name=request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['confirm_password']
        if password==con_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exist")
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already registered")
                return render(request,'register.html')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, password=password, email=email,
                        last_name=last_name)
                user.save();
        else:
            messages.info(request,"not matched")
            return render(request,'register.html')
        return redirect('/')
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
