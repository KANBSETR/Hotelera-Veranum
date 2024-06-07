
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('api/core/', include('core.api.urls')),
    path('core/', include('core.urls')),
]
