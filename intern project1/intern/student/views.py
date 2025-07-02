from django.shortcuts import render, redirect
from .forms import Signupform, Loginform
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Files
from django.http import FileResponse, Http404
import os
from django.conf import settings

# Create your views here.

def home(request):
    return render(request,'student/home.html')

def about(request):
    return render(request,'student/about.html')
  
def contact(request):
    return render(request,'student/contactus.html')

def edu(request):
    return render(request,'student/edumate.html')

def faculity(request):
    return render(request,'student/faculity.html')

def computer(request):
    return render(request,'student/computer.html')
def civil(request):
    return render(request,'student/civil.html')
def electronics(request):
    return render(request,'student/electronics.html')

def downsec(request):
    file = {'file':Files.objects.all()}
    return render(request,'student/downsec.html', file)

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True)
    else:
        raise Http404("File not found")





def user_signup(request):
    form = Signupform()
    if request.method =="POST":
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congrulations you have signed up')
    else:
        form = Signupform()
    return render(request,'student/signup.html', {'form': form})

# login
def user_login(request):
    if not request.user.is_authenticated:
        form = Loginform()
        if request.method == "POST":
            form = Loginform(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None: 
                    login(request, user)
                    messages.success(request, 'Congrulations you have successfully login! ')
                    return redirect('/home/')
        else:
            form = Loginform()
        return render(request,'student/login.html', {'form':form})
    else:
        return redirect('/dashboard/')