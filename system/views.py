from django.shortcuts import render, redirect,get_object_or_404
from .forms import CreateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login 
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 
from .forms import CategoryFilterForm
from .filters import ProductFilter





 
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
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
            return redirect('mylist')
    else: 
        form = ProductForm()   

    products = Product.objects.all()
    return render(request, 'system/list.html', {'products': products, 'form': form})


def index(request):
    products = Product.objects.all()
    category_filter_form = CategoryFilterForm(request.GET or None)

    if category_filter_form.is_valid():
        category = category_filter_form.cleaned_data.get('category')
        if category:
            products = products.filter(category=category) 

    return render(request, 'system/index.html', {'products': products,  'category_filter_form': category_filter_form})



def index_detail(request, pk):
    print('PK value:', pk)
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'system/index2.html', {'product': product}) 


def register(request):
    
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
        

        
        


    context = {'form':form}
    return render(request, 'system/register.html', context )

@login_required
def mylist(request):
 product  = Product.objects.filter(user=request.user)




 return render(request, 'system/mylist.html', {'products': product} )



def deleteItem(request, pk):
   product= get_object_or_404(Product, pk=pk, user=request.user)
   product.delete()  
   return redirect('mylist')      




def user_logout(request):
    logout(request)
    return redirect('index')


def update_item(request, pk):
    product = get_object_or_404(Product, pk=pk , user=request.user)
    form =  ProductForm(request.POST or None, instance = product)

    if form.is_valid():
        form.save()
        return redirect('mylist')
    else:
        print(form.errors)




     
    return render( request, 'system/updateItem.html', {'form': form, 'product': product})





# def clientList(request):



#  return render(request, 'system/clientList')
