from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# http://localhost:8000/api/test
@api_view(['GET'])
def test(request):
    return Response({'message': 'Hello, world!'})