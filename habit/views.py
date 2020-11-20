from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from .models import Habit
from .forms import FormHabit

# For do search of Cards
from django.db.models import Q


def create_habit(request):
    ''' Form used for create a new habit. '''

    data = {}
    form = FormHabit(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')
    data['form'] = form
    return render(request , 'habit_form.html', data)



class home(ListView):
    '''  '''
    model = Habit
    template_name = 'home.html'





def update_habit(request, pk):
    ''' Form used for update a habit already created. '''

    data = {}
    data['habit'] = Habit.objects.get(pk=pk)

    form = FormHabit(request.POST  or None, instance = data['habit'])

    if form.is_valid():
        form.save()
        return redirect('home')
    data['form'] = form
    return render(request , 'habit_form.html', data)



def delete_habit(request, pk):
    ''' Delete the habit with key = pk of db '''

    habit = Habit.objects.get(pk=pk)
    habit.delete()
    return redirect('home')




class SearchResultsView(ListView):
    '''
        Search per cards with start of name and exact level specified by the user.
        :param ListView: A page representing a list of objects.
    '''
    model = Habit
    template_name = 'home.html'

    def get_queryset(self): # new
        '''
            Catch the name or/and level specified per user;
            Do a filter in database;
            Keep a list of cards of search.
            :return object_list : list of cards of search.
        '''
        # Name specified per user;
        query_name = self.request.GET.get('q_name')
        object_list = Habit.objects.filter(
            Q(name__startswith=query_name)
        )
        return object_list