from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_habit, name="create_habit"),
    path('', views.home.as_view(), name="home"),
    path('update/<int:pk>', views.update_habit, name="update_habit"),
    path('delete/<int:pk>', views.delete_habit, name="delete_habit"),
    path('search/', views.SearchResultsView.as_view(), name="search"),
    
    


]
