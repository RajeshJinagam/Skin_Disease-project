from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'mainpage.html')

def login(request):
    return render(request,'loginpage.html')

def signup(request):
    return render(request,'signup.html')
