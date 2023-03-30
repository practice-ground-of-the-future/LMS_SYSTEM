from django.db import models
from users.models import User
from django.utils import timezone


# Create your models here.

class TaskCategory(models.Model):
    """Модель описывающая дисциплины для заданий"""
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    """Модель описывающая задания"""
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    exp = models.IntegerField(default=30)
    category = models.ForeignKey(to=TaskCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProfileTask(models.Model):
    """Модель описывающая задания пользотеля"""

    # Функция подсчёта deadline задания
    @staticmethod
    def get_dead_line():
        return timezone.now() + timezone.timedelta(days=7)

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    dead_line = models.DateTimeField(default=get_dead_line())
    success = models.BooleanField(default=False)

    def __str__(self):
        return f'задание для {self.user.email} / задание: {self.task.name}'


class FileModel(models.Model):
    """Модель описывающая отправленные задания"""

    profile_task = models.ForeignKey(to=ProfileTask, on_delete=models.CASCADE)
    file = models.FileField(upload_to='user_code')
    created_timestamp = models.DateTimeField(auto_now_add=True)