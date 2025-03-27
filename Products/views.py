from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category
# Create your views here.
def index(request):
    products=Product.objects.all()
    context ={
        'products':products
    }
    return render(request,'products/showproduct.html',context)

