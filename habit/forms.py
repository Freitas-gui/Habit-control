from django import forms
from .models import Habit

class FormHabit(forms.ModelForm):
    class Meta:
        model = Habit
        fields = {'name', 'trigger', 'routine', 'reward', 'good'}