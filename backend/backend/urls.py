
from django.contrib import admin
from django.urls import path, include
from . import views
from .views_serializer import router
from django.conf import settings
from django.conf.urls.static import static


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView



urlpatterns = [
    path('admin/', admin.site.urls),    
    path('api/core/', include(router.urls)),
    path('', include('core.urls')),
    path('habitaciones/',include('habitaciones.urls')),
    path('serviciosAd/',include('serviciosadicionales.urls')),
<<<<<<< HEAD
    path('inventario/',include('inventario.urls')),
=======
>>>>>>> 8b440665b871ba0a90c3da1b0d3f4c9c53eb5339
    path('eventos/',include('centroeventos.urls')),
    path('', views.LoadMenu.as_view()),
    path('frontend/', include('frontend.urls')),

    path('apix/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('apix/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('apix/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

] 


