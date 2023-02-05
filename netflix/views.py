
from django.shortcuts import render,redirect
from .models import movies
from django.contrib import messages
from django.contrib.auth.models import User , auth
# Create your views here.
def home(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def sign_in(request):
    return render(request,'sign_in.html')
def main2(request):
    imgs=movies.objects.all()
    name=request.POST['name']
    mail=request.POST['email']
    password1=request.POST['password']
    password2=request.POST['cpassword']
    l=[password1,password2,name,mail]
    if User.objects.filter(username=name).exists() :
        messages.info(request,'username was taken already')
        return redirect('register')
    if User.objects.filter(email=mail).exists() :
        messages.info(request,'email was taken already')
        return redirect('register')
    if password1!=password2 :
        messages.info(request,'both passwords are not matching')
        return redirect('register')
    else:
        if all(l):
            user=User.objects.create_user(username=name,email=mail,password=password1)
            user.save()
            return redirect('sign_in')
        else:
            messages.error(request,'input fields cannot be empty')
            return redirect('register')
def logout(request):
   auth.logout(request)
   return redirect('sign_in')

def main(request):
    mail=request.POST['email']
    password=request.POST['password']
    l=[mail,password]
    if all(l):
        u=User.objects.filter(email=mail)[0]
        user=auth.authenticate(username=u.username,password=password)
        if user is not None:
            imgs=movies.objects.all()
            auth.login(request,user)
            return render(request,'main.html',{'imgs':imgs})
        else:
            print(user,1)
            messages.info(request,'password tappu ra edava')
            return redirect('sign_in')
    else:
         messages.error(request,'input fields cannot be empty')
         return redirect('sign_in')
