
from django.shortcuts import render, redirect
from django.contrib import messages
 
# import todo form and models
 
from .forms import TodoForm
from .models import ToDo

# Create your views here.

def home(request):
    item_list = ToDo.objects.order_by("-date")
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TodoForm()
    page = {'forms':form,
            'list':item_list}
    return render(request,'todo.html',page)

def remove(request, item_id):
    item = ToDo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')