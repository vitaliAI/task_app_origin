from django.shortcuts import render
from .models import Task

def index(request):
    items = Task.objects.all()
    context = {'tasks': items}
    return render(request, 'task/task-list.html', context)

