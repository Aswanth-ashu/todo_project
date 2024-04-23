from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class TodoItem(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

