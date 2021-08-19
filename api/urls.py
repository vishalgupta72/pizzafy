from django.urls import path, include
# from . import views
from .serializers import router

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
