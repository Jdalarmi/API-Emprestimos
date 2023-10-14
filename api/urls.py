from django. urls import path, include
from . import views



urlpatterns = [
    path('registrar_pessoa/', views.registar_pessoa, name='registrar_pessoa'),
    
]