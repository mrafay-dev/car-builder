from django.urls import path
from .views import CarListCreate, CarDetail
from django.urls import path, include, re_path
from django.urls import path, include, re_path
from .views import FrontendAppView

urlpatterns = [
    path('cars/', CarListCreate.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarDetail.as_view(), name='car-detail'),
    re_path(r"^.*$", FrontendAppView.as_view(), name="home"),
]