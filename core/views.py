from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo, User


def create_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        
        if title:
            user = User.objects.first() 
            Todo.objects.create(title=title, description=description, user=user)
            return redirect("core:get_todos")
            
    return render(request, "create.html")



def get_todos(request):
    todos = Todo.objects.all()
    newtodos = []
    for todo in todos:
        newtodos.append(
            {
                "id": todo.id,
                "title": todo.title,
                "description": todo.description,
                "user": todo.user.username,
            }
        )
    print(newtodos)
    return render(request, "index.html", {"todo_lists": newtodos})


def get_todo_by_id(request, todo_id):
    find_todo = Todo.objects.get(pk=todo_id)
    if not find_todo:
        return HttpResponse("Todo not found", status=404)
    return render(request, "detail.html", {"todo": find_todo})


def update_todo(request):
    return HttpResponse("Update a todo")


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == "POST":
        todo.delete()
        return redirect("core:get_todos")
    return render(request, "delete.html", {"todo": todo})