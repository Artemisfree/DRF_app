from django.urls import path
from .views import MappackList, MappackDetail

urlpatterns = [
    path('mappacks/', MappackList.as_view(), name='mappack_list'),
    path('mappacks/<int:pk>/', MappackDetail.as_view(), name='mappack_detail'),
]
