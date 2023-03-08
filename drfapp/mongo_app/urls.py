from django.urls import path
from .views import get_mappack

urlpatterns = [
    path('mappacks/', get_mappack, name='get_mappack'),
]
