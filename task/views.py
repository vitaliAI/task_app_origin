from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Task
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class TaskListViewActive(LoginRequiredMixin, ListView):
    queryset = Task.active_objects.all()
    template_name = 'task/task-list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']


class TaskListViewDone(LoginRequiredMixin, ListView):
    queryset = Task.done_objects.all()
    template_name = 'task/task-list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']


class TaskListViewAll(LoginRequiredMixin, ListView):
    queryset = Task.objects.all()
    template_name = 'task/task-list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'is_finished']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'is_finished']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.creator:
            return True
        return False

    def get_success_url(self):
        return reverse('task:task-list')

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = '/'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.creator:
            return True
        return False
