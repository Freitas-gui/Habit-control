from django.shortcuts import render, redirect
from .models import Habit
from .forms import FormHabit



# Create your views here.
def home(request):
    return render(request,"home.html")

def create_habit(request):
    ''' Form used for create a new habit. '''

    data = {}
    form = FormHabit(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('show_all')
    data['form'] = form
    return render(request , 'habit_form.html', data)

def show_all(request):
    ''' Show all habits that existed in db '''

    data = {}
    habits = Habit.objects.all()
    data['habits'] = habits
    return render(request, 'show_all.html',data)

def update_habit(request, pk):
    ''' Form used for update a habit already created. '''

    data = {}
    data['habit'] = Habit.objects.get(pk=pk)

    form = FormHabit(request.POST  or None, instance = data['habit'])

    if form.is_valid():
        form.save()
        return redirect('show_all')
    data['form'] = form
    return render(request , 'habit_form.html', data)

def delete_habit(request, pk):
    ''' Delete the habit with key = pk of db '''

    habit = Habit.objects.get(pk=pk)
    habit.delete()
    return redirect('show_all')
