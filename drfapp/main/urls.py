from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send_hex_file/', views.upload_hex_file, name='upload_hex_file'),
    path('recive_hex_file/', views.recive_hex_file, name='recive_hex_file'),
]
