from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product, Category
from django.contrib import messages
# Create your views here.

# To Show Product
def index(request):
    products=Product.objects.all()
    context ={
        'products':products
    }
    return render(request,'products/showproduct.html',context)

# To Show Category
def show_category(request):
    category =Category.objects.all()
    context = {
        'category' :category
    }
    return render(request, 'products/showcategory.html',context)

# To Delete Category
def delete_category(request,category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request,messages.SUCCESS,'Category Deleted')
    return redirect('/Products/categorylist')

# To Delete Product
def delete_product(request,product_id):
    product = Product.objects.get(id = product_id)
    product.delete()
    messages.add_message(request,messages.SUCCESS,'Product Deleted')
    return redirect('/Products/list')

