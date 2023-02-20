from django.urls import path
from . import views


urlpatterns = [
    path('send_hex_file/', views.upload_hex_file),
    path('recive_hex_file/', views.receive_hex_file),
]
