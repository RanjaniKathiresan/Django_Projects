
from django.shortcuts import render, redirect
from django.contrib import messages
 
# import todo form and models
 
from .forms import TodoForm
from .models import ToDo

# Create your views here.

def home(request):
    form = TodoForm()
    return render(request,'todo.html',{'forms':form})
