from django.urls import path 
from . import views


urlpatterns = [
    path('', views.getRoute),
    path('product/', views.getProducts),
    path('product/<str:pk>/', views.getProduct)

]