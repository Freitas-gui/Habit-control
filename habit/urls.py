from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('create/', views.create_habit, name="create_habit"),
    path('show/all/', views.show_all, name="show_all"),
]
