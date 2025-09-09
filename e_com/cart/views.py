from django.shortcuts import render, redirect, get_object_or_404
# from .models import Cart, CartItem
from .cart  import Cart
from storeapp.models import Products
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    # cart = Cart.objects.get(user=request.user)
    # items = CartItem.objects.filter(cart=cart)
    # products = []
    # total = 0
    # for item in items:
    #     product_data = {
    #         'id': item.product.id,
    #         'name': item.product.name,
    #         'quantity': item.quantity,
    #         'price': item.product.price,
    #         'total_price': item.quantity * item.product.price,
    #     }
    #     products.append(product_data)
    #     total += product_data['total_price']
    return render(request, 'cart_summary.html',{})

def cart_add(request):
    cart =Cart(request)
    #posting
    if request.POST.get("action")=='post':
        product_id=int(request.POST.get('product_id'))
        #product in db
        Product=get_object_or_404(Products,id=product_id)
        #save to session
        cart.add(product=Product)  # Pass the actual product instance, not the Products class
        #return response 
        # response=JsonResponse({'product Name': Product.name})
        chart_quantity =cart.__len__()
        response =JsonResponse({'qty' :chart_quantity})
        return response
    
def cart_delete(request, product_id):
    pass
def cart_update(request):
    pass