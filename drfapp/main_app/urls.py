from django.urls import path
from . import views

urlpatterns = [
    path('send-file/', views.send_file, name='send_file'),
    path('receive-file/', views.receive_file, name='receive_file'),
]
