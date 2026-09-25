from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from .models import Product, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from .cart import Cart
from django.views.decorators.csrf import csrf_protect
# Create your views here.

@csrf_protect
def add_to_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = Product.objects.get(product_id=product_id)

        cart.add(product=product)
        cart_quantity = cart.__len__()

        data = {"Cart_Quantity":cart_quantity,
                "product_name":product.product_name,
                "product_category":product.product_category.category_name,
                "product_id":product_id,
                "product_img_url":product.product_img.url,
                "product_price":product.product_price,
                "product_previous":product.product_previous,}

        return JsonResponse(data)

@csrf_protect
def update_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = Product.objects.get(product_id=product_id)
        product_qty = int(request.POST.get('product_qty'))

        cart.update_qty(product_id=product_id, qty=product_qty)

        return JsonResponse({product_id:product_qty})
    
@csrf_protect
def delete_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        cart_quantity = cart.__len__()
        cart.delete(product_id=product_id)

        return JsonResponse({"product_id":product_id,
                             "Cart_Quantity":cart_quantity})

@login_required(login_url='login')
def addon(request):
    if request.method == "POST":
        dOB = request.POST.get("date_of_birth")
        sex = request.POST.get("gender")
        username = request.user.username
        User.objects.filter(username=username).update(date_of_birth=dOB, sex=sex)
        return redirect('addon-2')

    return render(request, "register_addons/addons.html")

@login_required(login_url='login')
def addon_2(request):
    if request.method == 'POST':
        return redirect('addon-3')
    
    return render(request, "register_addons/addons-2.html")

@login_required(login_url='login')
def addon_3(request):
    if request.method == "POST":
        bio = request.POST.get("bio")
        profile_pic = request.POST.get("profile-pic")
        username = request.user.username
        User.objects.filter(username=username).update(bio=bio, profile_pic=profile_pic)
        return redirect('home-intro')

    return render(request, "register_addons/addons-3.html")

def page_404(request, exception):
    return render(request, "404.html")

def about(request):
    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper

    return render(request, "about.html")

def article(request):
    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper

    return render(request, "article.html")

def blog_full(request):
    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper

    return render(request, "blog-grid-fullpage.html")

def blod_grid(request):
    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper

    return render(request, "blog-grid.html")

def blog_list(request):
    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper

    return render(request, "blog-list.html")

def category(request):
    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper

    return render(request, "category.html")

def checkout_1(request):
    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper
 
    return render(request, "checkout-1.html")

def checkout_2(request):
    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper   

    return render(request, "checkout-2.html")

def checkout_3(request):
    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper

    return render(request, "checkout-3.html")

def checkout_4(request):
    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper

    return render(request, "checkout-4.html")

def contact(request):
    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper

    return render(request, "contact.html")

def email_receipt(request):
    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper

    return render(request, "email-receipt.html")

def ideas(request):
    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper
    return render(request, "ideas.html")

def home(request):
    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper

    product = Product.objects.get(product_id=1)
    context = {"product": product}
    return render(request, "index.html", context)


def home_tabsy(request):
    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper

    product = Product.objects.get(product_id=1)
    context = {"product": product}
    return render(request, "index-2.html", context)

def home_intro(request):

    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper

    return render(request, "index-3.html")

def login_page(request):
    form = UserForm()
    if request.method == 'POST' and request.POST.get('username') is None:
        
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "User Doesn`t exist")


        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
    if request.method == "POST" and request.POST.get("username") is not None:
        user = User(first_name=request.POST.get("first_name"),
                    last_name=request.POST.get("last_name"),
                    username=request.POST.get("username"),
                    email=request.POST.get("email"),
                    password=request.POST.get("password"),)
        user.save()

        login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        return redirect('home-intro')
        
    context = {}
        
    return render(request, 'login.html', context)

def product(request, pak):
    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper
    
    product = Product.objects.get(product_id=pak)
    context = {"product":product,}

    return render(request, "product.html", context)

def product_grid_intro(request):
    cart = Cart(request)
    cart_products = cart.get_products()
    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper
    
    context = {"cart_products": cart_products}

    return render(request, "products-grid-intro.html", context)

def product_grid(request):
    cart = Cart(request)
    # Search --wrapper
    hunt = request.GET.get('hunt') if request.GET.get('hunt') != None else ''

    products = Product.objects.filter(
        Q(product_name__icontains=hunt) |
        Q(product_category__category_name__icontains=hunt)|
        Q(product_brand__brand_name__icontains=hunt) |
        Q(product_model__icontains=hunt) |
        Q(product_type__type_name__icontains=hunt)
    )
    # Search --wrapper

    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper

    context = {
        "products":products,
    }

    return render(request, "products-grid.html", context)

def product_list(request):
    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper

    return render(request, "products-list.html")

def product_topbar(request):
    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper

    return render(request, "products-topbar.html")

def shortcodes(request):
    # -- Navigation bar login -- wrapper 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
        except:
            messages.error(request, "Incorrect Username or Password")

        if user is not None:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
    # Navigation bar login wrapper

    return render(request, "shortcodes.html")