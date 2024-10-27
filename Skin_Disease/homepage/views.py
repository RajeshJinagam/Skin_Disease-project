from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate

def main(request):
    return render(request,'mainpage.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('/profile')  

    if request.method == "POST":
        un = request.POST['username']
        pw = request.POST['password']
        user = authenticate(request, username=un, password=pw)
        if user is not None:
            return redirect('/profile')  
        else:
            msg = 'Invalid Username/Password'
            return render(request, 'loginpage.html', {'msg': msg})
    else:
        return render(request, 'loginpage.html')


def signup(request):
     if(request.user.is_authenticated):
         return redirect('/')
     if(request.method == "POST"):
         un = request.POST['username']
         pw1 = request.POST['password']
         pw2 = request.POST['confirmPassword']
         user = authenticate(request,username=un)
         print(user)
         if(user is not None):
             if(pw1==pw2):
                 authenticate(username=un,password=pw1)
                 return redirect('/login')
             else:
                 msg = 'Incorrect password!'
                 return render(request,'signup.html',{'msg':msg})
         else:
             msg = 'User already registered!'
             return render(request,'signup.html',{'msg':msg})
     else:
         return render(request,'signup.html')

def profile(request):
    return render(request,'profile.html')