from django.shortcuts import render, redirect
from .forms import Signupform, Loginform, PostEmployee
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import intern
# Create your views here.

def home(request):
    return render(request,'intern/home.html')

def about(request):
    return render(request,'intern/about.html')
  
def contact(request):
    return render(request,'intern/contactus.html')
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
                    return redirect('/addpost/')
        else:
            form = Loginform()
        return render(request,'intern/login.html', {'form':form})
    else:
        return redirect('/dashboard/')
    

def user_signup(request):
    form = Signupform()
    if request.method =="POST":
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congrulations you have signed up')
    else:
        form = Signupform()
    return render(request,'intern/signup.html', {'form': form})
    
#dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts= intern.objects.all()
        return render(request,'intern/dashboard.html', {'posts':posts})
    else:
        return redirect('/login/')
# logout
def user_logout(request):
    logout(request)
    return redirect('/')
# Add newpost
def add_post(request):
      if request.user.is_authenticated:
        form=PostEmployee() 
        if request.method =='POST':
                form = PostEmployee(request.POST, request.FILES)
                if form.is_valid():
                    fn = form.cleaned_data['firstname']
                    ln = form.cleaned_data['lastname']
                    el = form.cleaned_data['email']
                    pe = form.cleaned_data['phone']
                    loc = form.cleaned_data['location']
                    ed = form.cleaned_data['college']
                    jb = form.cleaned_data['job']
                    fl = form.cleaned_data['myfile']
                    form=intern(firstname=fn,lastname=ln,email=el, phone=pe,location=loc,college=ed, job=jb, myfile=fl)
                    form.save()
                    form=PostEmployee()   
        else:
            form=PostEmployee()   
        return render(request, 'intern/addpost.html',{'form':form}) 
            
      else:    
        return redirect('/login/')
    
    
# Add updatepost
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method =='POST':
            pi = intern.objects.get(pk=id)
            form = PostEmployee(request.POST, request.FILES, instance=pi, )
            if form.is_valid():
                form.save()
                form = PostEmployee()   
        else:
            pi = intern.objects.get(pk=id)
            form = PostEmployee(instance=pi)        
        return render(request, 'intern/updatepost.html',{'form':form})
    else:
        return redirect('/login/')

 # Delete post
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method =='POST':
            pi = intern.objects.get(pk=id)
            pi.delete()
            return redirect('/dashboard/')
    else:
        return redirect('/login/')

