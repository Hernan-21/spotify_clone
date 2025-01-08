from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('callback', views.callback, name='callback'),
    path('playlist/<str:playlist_id>/', views.playlist_detail, name='playlist_detail'),
] 