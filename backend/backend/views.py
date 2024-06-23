from rest_framework.views import APIView
from django.http import JsonResponse

class LoadMenu(APIView):
    def get(self, request, format=None):
        return JsonResponse({'BACKEND': 'http://localhost:9098/habitaciones/backend/'
                            ,'API': 'http://localhost:9098/api/core/'
                            ,'Administrador':'http://localhost:9010/admin'
                            ,'Load':'http://localhost:9098/habitaciones/load/'
                            ,'Html':'http://localhost:9098/frontend/index/'
                            })
    
