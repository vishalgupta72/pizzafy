from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('api-auth/', include('rest_framework.urls'))
]
