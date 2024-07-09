from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class Tasks(models.Model):
    task_name = models.CharField(max_length=20)
    description = models.TextField( default="")
    status = models.CharField(max_length=15, default="uncompleted")
    date = models.DateField(default=timezone.now)
    class Meta:
        db_table = "tasks"

