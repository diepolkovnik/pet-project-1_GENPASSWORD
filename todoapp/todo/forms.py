from django.forms import ModelForm, fields
from .models import *

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']