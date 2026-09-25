from .cart import Cart

def cart(request):
    #Return data from cart
    return {'cart':Cart(request)}

def cart_products(request):
    cart = Cart(request)
    cart_products = cart.get_products()
    return {"cart_products":cart_products}