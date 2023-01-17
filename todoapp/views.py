from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.
# def todo_list(request):
#     return HttpResponse("Hello world")
def todo_list2(request):
    return render(request, "todo_list2.html")

def todo_list(request):
    todos = Todo.objects.all()
    print(todos)

    context = {
        "todo_list" : todos
    }

    return render(request, "todoapp/todo_list.html", context)

def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo" : todo
    }

    return render(request, "todoapp/todo_detail.html", context)

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/home")
    context = {
        "form" : form
    }

    return render(request, "todoapp/todo_create.html", context)

def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect("/home")
    context = {
        "form" : form
    }

    return render(request, "todoapp/todo_update.html", context)

def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()

    return redirect("/home")