from django.urls import path
from .views import authenticate_user

urlpatterns = [
    path('authenticate/', authenticate_user, name='authenticate_user'),
]
