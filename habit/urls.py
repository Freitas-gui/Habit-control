from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('create/', views.create_habit, name="create_habit"),
    path('show/all/', views.show_all, name="show_all"),
    path('update/<int:pk>', views.update_habit, name="update_habit"),
    path('delete/<int:pk>', views.delete_habit, name="delete_habit"),


]
