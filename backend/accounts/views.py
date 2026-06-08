from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

@api_view(['POST'])
def register(request):

    data = request.data

    if User.objects.filter(username=data['username']).exists():

        return Response({
            'message':'User already exists'
        })

    user = User.objects.create(

        username=data['username'],
        email=data['email'],
        password=make_password(data['password'])

    )

    return Response({
        'message':'User registered successfully'
    })
