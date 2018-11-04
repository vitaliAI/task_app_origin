from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class TaskManagerActive(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_finished=False)


class TaskManagerDone(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_finished=True)


class Task(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    finished_at = models.DateTimeField(null=True)
    is_finished = models.BooleanField(default=False)
    creator = models.ForeignKey(User, null=True, related_name='crator', on_delete=models.CASCADE)

    objects = models.Manager()
    active_objects = TaskManagerActive()
    done_objects = TaskManagerDone()

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.title

    def close(self):
        self.is_finished = True
        self.finished_at = timezone.now()
        self.save()

    def reopen(self):
        self.is_finished = False
        self.finished_at = None
        self.save()

    def get_absolute_url(self):
        return reverse('task:task-detail', kwargs={'pk': self.pk})
