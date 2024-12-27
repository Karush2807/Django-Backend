from django.shortcuts import render
from .serializers import RoomSerializer
from rest_framework import generics
from .models import Room

# Create your views here.
class Roomview(generics.ListAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer