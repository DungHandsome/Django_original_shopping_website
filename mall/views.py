from django.shortcuts import render
from .models import Product
# Create your views here.
def mall(request):
    Data = {'Products': Product.objects.all().order_by('-date')}
    return render(request, 'mall/mall.html', Data)
def products(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product.html', {'product': product})