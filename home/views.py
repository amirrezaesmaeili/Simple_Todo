from django.shortcuts import render
from .models import Todo

def home(request):
    todo_info = Todo.objects.all()
    return render(request,'home.html',context={'todos':todo_info})

def detail(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request,'detail.html',{'todo':todo})