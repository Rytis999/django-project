from django.shortcuts import render,redirect, get_object_or_404
from .models import Car ,Cart
from django.contrib.auth import authenticate , login 
from django.contrib.auth.decorators import login_required

# Create your views here.


def rent_index(request):
 cars  = Car.objects.all()

 return render(request, 'rent/index.html', {'cars': cars })



def  rent_detail(request, pk):
    print('PK value:', pk)
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'rent/index2.html', {'car': car}) 

 
 
@login_required
def add_to_cart(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        cart_item, created = Cart.objects.get_or_create(user=request.user, car=car, start_date=start_date, end_date=end_date)
        return redirect('cart_view')
    return render(request, 'rent/add_to_cart.html', {'car': car})

@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'rent/cart.html', {'cart_items': cart_items})


