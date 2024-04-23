from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem, Project
from .forms import ProjectForm,TodoItemForm
from .models import Task

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'todo/project_list.html', {'projects': projects})

def project_todo_list(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    todos = TodoItem.objects.filter(project=project)
    return render(request, 'todo/project_todo_list.html', {'project': project, 'todos': todos})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'todo/project_create.html', {'form': form})

def project_update(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'todo/project_update.html', {'form': form, 'project': project})

def project_delete(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'todo/project_confirm_delete.html', {'project': project})

def todo_create(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.project = project
            todo.save()
            return redirect('project_todo_list', project_id=project_id)
    else:
        form = TodoItemForm()
        
    return render(request, 'todo/todo_create.html', {'form': form, 'project': project})

def todo_update(request, project_id, todo_id):
    todo = get_object_or_404(TodoItem, pk=todo_id)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('project_todo_list', project_id=project_id)
    else:
        form = TodoItemForm(instance=todo)
    return render(request, 'todo/todo_update.html', {'form': form, 'project_id': project_id, 'todo_id': todo_id})

def todo_delete(request, project_id, todo_id):
    todo = get_object_or_404(TodoItem, pk=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('project_todo_list', project_id=project_id)
    return render(request, 'todo/todo_confirm_delete.html', {'todo': todo})



