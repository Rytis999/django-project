from django.urls import path

from . import views
 

urlpatterns = [
    path('', views.rent_index, name='rent_index'),
    path('<int:pk>/', views.rent_detail, name='rent_detail'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('addcar/', views.addcar, name='addcar'),
    path('my-rents/', views.my_rents, name='my_rents'),
]

