from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('register', views.register,  name = 'register'), 
    path('login', views.user_login, name = 'login'),
    path('logout', views.user_logout, name='user_logout'),
    path('list/', views.list, name = 'list'),
    path('<int:pk>/', views.index_detail, name='index_detail'),
    path('mylist', views.mylist, name= 'mylist' ),
    # path('clientList', views.clientList, name = 'clientList'),
    path('delete/<int:pk>/', views.deleteItem, name='deleteItem'),
    path('updateItem/<int:pk>/', views.update_item, name='updateItem'  ),
    
 
    

    
]
