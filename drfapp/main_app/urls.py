from django.urls import path
from . import views

urlpatterns = [
    path('get_options/', views.get_options, name='get_options'),
    path('patch_file/', views.patch_file, name='patch_file'),
]
