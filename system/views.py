from django.shortcuts import render, redirect
from .forms import CreateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login 
from .models import Product
from .forms import ProductForm




 
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('list')
        else:
             
            error_message = 'Invalid username or password'
            return render(request, 'system/login.html', {'error_message': error_message})
 
    return render(request, 'system/login.html') 


 

def list(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else: 
        form = ProductForm()   

    products = Product.objects.all()
    return render(request, 'system/list.html', {'products': products, 'form': form})


def index(request):
    products = Product.objects.all()
    return render(request, 'system/index.html', {'products': products})
 

 


def register(request):
    
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
        

        
        


    context = {'form':form}
    return render(request, 'system/register.html', context )



