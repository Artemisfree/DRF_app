from django.urls import path
from .views import MappackView

urlpatterns = [
    path(
        'mappacks/<str:name>/<str:brand>/<str:ecu>/<str:software_version>/',
        MappackView.as_view(),
        name='mappack-detail'
    ),
]
