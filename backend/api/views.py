from django.shortcuts import render
from rest_framework import generics
from .models import Car
from .serializers import CarSerializer
# backend/views.py
from django.views.generic import TemplateView

class FrontendAppView(TemplateView):
    template_name = "index.html"


class CarListCreate(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


