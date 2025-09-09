from .cart import Cart
#crete context processor to work  cart on all the pages
def cart(request):
    #rtn default data from Cart
    return {'cart':Cart(request)}
