from django.shortcuts import render
from .models import Todo
def say_hello(request):
    user = {"name":"reza"}
    return render(request,'hello.html',context=user)

def home(request):
    todo_info = Todo.objects.all()
    return render(request,'home.html',context={'todos':todo_info})