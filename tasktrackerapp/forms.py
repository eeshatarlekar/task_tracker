from django import forms
from django.contrib.auth.models import User
from .models import User,Project,Tasks
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import NumberInput



class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2','department','designation']

class ProjectForm(forms.ModelForm):
    deadline = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model=Project
        fields=['proj_name','description','deadline']

    

class TasksForm(forms.ModelForm):
    start_time=forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    end_time=forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

    class Meta:
        model=Tasks
        fields=['task_name','start_time','end_time']
