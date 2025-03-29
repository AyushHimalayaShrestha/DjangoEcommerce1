from django.urls import path
from .views import *



urlpatterns =[
    path('list/', index ),
    path('categorylist/',show_category),
    path('deletecategory/<int:category_id>',delete_category),
    path('deleteproduct/<int:product_id>',delete_product),

   
]