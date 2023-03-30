from django.contrib import admin

# Register your models here.

from firstapp.models import TaskCategory, Task, FileModel

admin.site.register(Task)
admin.site.register(TaskCategory)
admin.site.register(FileModel)


