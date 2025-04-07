from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product, Category
from django.contrib import messages
from .forms import CategoryForm,ProductForm
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
    product = Product.objects.get(id =product_id)
    product.delete()
    messages.add_message(request,messages.SUCCESS,'Product Deleted')
    return redirect('/Products/list')

# To Post Category
def post_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Category Added')
            return redirect('/Products/postcategory')
        else:
            messages.add_message(request,messages.ERROR,'Please Verify Form Fields')
            return render(request,'products/addcategory.html',{'forms':form})
    context ={
        'forms': CategoryForm
    }
    return render(request,'Products/addcategory.html',context)

# To Post Product
def post_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Product Added')
            return redirect('/Products/postproduct')
        else:
            messages.add_message(request,messages.ERROR,'Please Verify Form Fields')
            return render(request,'products/addproduct.html',{'forms':form})
    context ={
        'forms': ProductForm
    }
    return render(request,'Products/addproduct.html',context)

# To Update Category
def update_category(request, category_id):
    instance =Category.objects.get(id=category_id)
    if request.method == 'POST':
        form=CategoryForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'Category Updated')
            return redirect('/Products/categorylist')
        else:
            messages.add_message(request,messages.ERROR,'Please verify form fields')
            return render(request,'Products/updatecategory.html',{'forms':form})

    context = {
        'forms': CategoryForm(instance=instance)
    }
    return render(request,'Products/updatecategory.html',context)
