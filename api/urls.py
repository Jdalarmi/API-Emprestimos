from django. urls import path, include
from . import views



urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('pessoa/', views.pessoa, name='pessoa'),
    path('registrar_pessoa/', views.getPessoa, name='registrar_pessoa'),
    
]