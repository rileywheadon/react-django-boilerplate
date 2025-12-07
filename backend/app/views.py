from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

def index(request):
    return render(request, 'app/index.html')

@api_view(['GET'])
def hello_api(request):
    return Response({
        'message': 'Hello from Django API!',
        'status': 'success'
    })
