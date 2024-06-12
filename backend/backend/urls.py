
from django.contrib import admin
from django.urls import path, include
from . import views
from .views_serializer import router
urlpatterns = [
    path('admin/', admin.site.urls),    
    path('api/core/', include('core.api.urls')),
    path('core/', include('core.urls')),
    path('habitaciones/',include('habitaciones.urls')),
    path('', views.LoadMenu.as_view()),
    path('frontend/', include('frontend.urls')),


]
