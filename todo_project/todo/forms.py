from django import forms
from .models import Project, TodoItem

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields ='__all__'
