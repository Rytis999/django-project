from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('register', views.register,  name = 'register'), 
    path('login', views.user_login, name = 'login'),
    path('list', views.list, name = 'list'),
    path('<int:pk>/', views.index_detail, name='index_detail'),
    path('items/', views.mylist, name= 'mylist' )

    
]
