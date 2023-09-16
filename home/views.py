from django.shortcuts import render

def say_hello(request):
    user = {"name":"reza"}
    return render(request,'hello.html',context=user)

def home(request):
    return render(request,'home.html')