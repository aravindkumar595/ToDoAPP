from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def home(request):
    if request.method == "POST":
        task_text = request.POST.get("task")
        if task_text:
            Task.objects.create(task=task_text)
        return redirect('home')

    tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)

    return render(request, 'home.html', {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    })


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.task = request.POST.get("task")
        task.save()
        return redirect('home')

    return render(request, 'edit.html', {'task': task})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')
