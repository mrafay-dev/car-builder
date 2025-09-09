from django.urls import path
from .views import CarListCreate, CarDetail

urlpatterns = [
    path('cars/', CarListCreate.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarDetail.as_view(), name='car-detail'),

]