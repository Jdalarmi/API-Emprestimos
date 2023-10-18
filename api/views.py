from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from .serializer import PessoaSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='post', request_body=PessoaSerializer)
@api_view(['POST'])
def registar_pessoa(request):
   """
    Esse endpoint registra pessoa:
    """
   serializer = PessoaSerializer(data=request.data)
   if serializer.is_valid():
       customer = serializer.data.get('name')
       income = float(serializer.data.get('income'))
       age = int(serializer.data.get('age'))
       location = str(serializer.data.get('location'))
       
       
       return Response(check_salario(income, customer, age, location))
   return (HttpResponse('Erro'))


def check_salario(salario, customer, age, location):
    pessoal = {
                    "customer": customer,
                    "loans": "PERSONAL",
                    "interest_rate" : 4
                }
    garantia = {
                    "customer": customer,
                    "loans": "GUARANTEED",
                    "interest_rate" : 4
                }
    consignado = {
                    "customer": customer,
                    "loans": "CONSIGNMENT",
                    "interest_rate" : 4
                }
    block = {
                    "customer": customer,
                    "loans": 'Você não se enquadra em nenhuma opcão de emprestimo'
                }
    
    lista_resultado = []
    resultado_emprestimo = {"loans":lista_resultado}
    

    if salario <= 3000:
        
        lista_resultado.append(pessoal)
        lista_resultado.append(garantia)
        return resultado_emprestimo
    elif salario > 3000 and salario <= 5000 and age < 30 and location == 'SP':
        
        lista_resultado.append(pessoal)
        lista_resultado.append(garantia)
        return resultado_emprestimo
    
    elif salario > 5000:
        
        lista_resultado.append(consignado)
        return resultado_emprestimo

    else:
        
        lista_resultado.append(block)
        return resultado_emprestimo

    


