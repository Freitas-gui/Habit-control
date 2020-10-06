from django.shortcuts import render, redirect
from .models import Habit
from .forms import FormHabit



# Create your views here.
def home(request):
    return render(request,"home.html")

def create_habit(request):
    ''' Form used for create a new habit. '''
    data = {}
    form = FormHabit(request.POST)

    if form.is_valid():
        form.save()
        return redirect('home')
    data['form'] = form
    return render(request , 'show_all.html' , data)

def show_all(request):
    data = {}
    habits = Habit.objects.all()
    data['habits'] = habits
    return render(request, 'show_all.html',data)