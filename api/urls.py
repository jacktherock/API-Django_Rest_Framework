from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_tracks, name='add-tracks'),
    path('all/', views.view_tracks, name='view-tracks'),
    path('update/<int:pk>/', views.update_tracks, name='update-tracks'),
    path('track/<int:pk>/delete/', views.delete_tracks, name='delete-tracks'),
]
