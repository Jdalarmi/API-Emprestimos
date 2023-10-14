from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from .serializer import PessoaSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
    ]
    return Response(routes)

@api_view(['POST'])
def pessoa(request):
   serializer = PessoaSerializer(data=request.data)
   if serializer.is_valid():
       serializer.save()
       print('armazenado no banco')
       return Response(serializer.data)
   return (HttpResponse('Erro'))

@api_view(['GET'])
def getPessoa(request):
    person = {
        "age": 26,
        "cpf": "275.484.389-23",
        "name": "Vuxaywua Zukiagou",
        "income": 7000.00,
        "location": "SP"
    }
    return Response(person)