from .models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        # If session exists grab cart from sessions key
        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product):
        product_id = str(product.product_id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] =  1 
        
        self.session.modified = True

    def update_qty(self, product_id, qty):
        cart = self.cart
        cart[product_id] = qty

        self.session.modified = True

    def delete(self, product_id):
        cart = self.cart
        del cart[str(product_id)]

        self.session.modified = True


    def __len__(self):
        return len(self.cart)
    
    def get_products(self):
        product_ids = self.cart.keys()
        product_qties = self.cart.values()
        products = Product.objects.filter(product_id__in=product_ids)
        itemz = {k: v for k, v in zip(products, product_qties)}
        return itemz
    
    