from django.shortcuts import render
from django.contrib.auth.models import User
from django_app.models import UserProfileInfo
from django_app.forms import UserForm,UserProfileInfoform
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
# Create your views here.

def user(request):
    return render(request,'one.html',context=None)
def register(request):
    registered = False
    if request.method == "POST":
        print('vishnu1')
        user = UserForm(data=request.POST)
        profile = UserProfileInfoform(data=request.POST)
        if user.is_valid() and profile.is_valid():
            usr=user.save()
            usr.set_password(usr.password)
            usr.save()
            pro=profile.save(commit=False)
            pro.user = usr
            if 'profile_pic' in request.FILES:
                pro.profile_pic = request.FILES['profile_pic']
            pro.save()
            registered = True
    else:
        user = UserForm()
        profile = UserProfileInfoform()

    return render(request,'register.html',{'user':user,'profile':profile,'registered':registered})
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('intro'))
            else:
                return HttpResponse("account not active")
        else:
            return HttpResponse('wrong login details')
    else:
        return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('intro'))
