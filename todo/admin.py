from django.contrib import admin
from.models import Project,TodoItem
from models import Task

# Register your models here.
admin.site.register(Project)
admin.site.register(TodoItem)
admin.site.register(Task)