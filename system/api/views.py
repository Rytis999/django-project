from rest_framework.decorators import api_view
from rest_framework.response import Response
from  system.models import Product 
from .serializers import ProductSerializer

@api_view(['GET'])
def getRoute(request):
    routes = [
        'GET/api',
        'GET/api/product',
        'GET/api/product/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product )
    return Response(serializer.data)


