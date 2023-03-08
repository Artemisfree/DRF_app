from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('postgre_app.urls')),
    path('mappack/', include('mongo_app.urls')),
    path('main/', include('main_app.urls')),
]
