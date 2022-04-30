from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def index(request):
    tasks=Task.objects.all()
   
    # return HttpResponse(tasks)
    return render(request,'index.html',{'tasks':tasks})

def add_form(request):
    if request.method=="POST":
        name=request.POST.get("name")
        priority=request.POST.get("priority")
        task=Task(name=name,priority=priority)
        task.save()
        return redirect('/')
    return render(request,'add.html')

def delete(request,id):
        if request.method=="POST":
                task=Task.objects.get(id=id)
                task.delete()
                return redirect('/')
        return render(request,'delete.html')    