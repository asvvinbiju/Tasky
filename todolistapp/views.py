from django.shortcuts import render, HttpResponse, redirect
from .models import Tasks

def task(request):
    t = Tasks.objects.all()
    return render(request, "task.html", {"data":t})

def add_task(request):
    if request.method == "POST":
        t_name = request.POST['task_name']
        desc = request.POST['desc']
        date = request.POST['date']
        t = Tasks.objects.create(task_name=t_name, description=desc, date=date)
        t.save()
        return redirect(task)
    else:
        return render(request, 'add_task.html')

def deletetask(request, id):
    t = Tasks.objects.get(id=id)
    t.delete()
    return redirect(task)

def completetask(request, id):
    t = Tasks.objects.get(id=id)
    t.status = 'completed'
    t.save()
    return redirect(task)