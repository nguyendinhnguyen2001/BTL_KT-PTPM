from django.http import JsonResponse
from django.shortcuts import redirect, render
from store.forms import LoginForm
from store.forms import CustomerRegistrationForm, CustomerProfileForm
from store.models import Customer, Product, Cart, OrderPlaced
from django.views import View
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProductView(View):
    def get(self, request):
        countCart = 0
        product1 = Product.objects.filter(brand='f0')
        product2 = Product.objects.filter(brand='f1')
        if request.user.is_authenticated:
            countCart = len(Cart.objects.filter(user=request.user))
        # product_nam = Product.objects.filter(category='san pham nam')
        # print(product_nam)
        return render(request, 'app/home.html', {'product_deals': product1, 'countCart': countCart, 'product_trends': product2})


class show_productView(View):
    def get(self, request):
        countCart = 0
        products = Product.objects.all()
        if request.user.is_authenticated:
            countCart = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/product.html', {'products': products, 'countCart': countCart})


class show_product_women(View):
    def get(self, request):
        countCart = 0
        if request.user.is_authenticated:
            countCart = len(Cart.objects.filter(user=request.user))
        products = Product.objects.all()
        productWomens = Product.objects.filter(category='san pham nu')
        productMens = Product.objects.filter(category='san pham nam')
        return render(request, 'app/productWomen.html', {'products': products, 'productWomens': productWomens, 'productMens': productMens, 'countCart': countCart})


class show_product_men(View):
    def get(self, request):
        countCart = 0
        if request.user.is_authenticated:
            countCart = len(Cart.objects.filter(user=request.user))
        products = Product.objects.all()
        productWomens = Product.objects.filter(category='san pham nu')
        productMens = Product.objects.filter(category='san pham nam')
        return render(request, 'app/productMen.html', {'products': products, 'productWomens': productWomens, 'productMens': productMens, 'countCart': countCart})


class ProductDetailView(View):
    def get(self, request, pk):
        countCart = 0
        product = Product.objects.get(pk=pk)
        item_in_cart = False
        if request.user.is_authenticated:
            countCart = len(Cart.objects.filter(user=request.user))
            for item in Cart.objects.filter(user=request.user):
                if pk == item.product.id:
                    item_in_cart = True
        data = {'product': product,
                'check_item': item_in_cart, 'countCart': countCart}
        return render(request, 'app/productdetail.html', data)


# class CartView(View):
#     def post(self, request, pk):
#         data = request.POST.get()
#         product = data.get('product')
#         quantity = data.get('quantity')
#         cart = Cart(user.id, product.id, quantity)
#         cart.save()
#         return render(request, 'app/home.html')
# class CartDetailView(View):
# def home(request):
#     return render(request, 'app/home.html')


# def product_detail(request):
#     return render(request, 'app/productdetail.html')

@login_required
def add_to_cart(request):
    user = request.user
    product = Product.objects.get(id=request.GET.get('prod_id'))
    cart = Cart(user=user, product=product)
    cart.save()
    return redirect('/cart')


@login_required
def show_cart(request):

    if request.user.is_authenticated:
        # data = request.POST
        # print(data)
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 5.0
        total_amount = 0.0
        if cart.count():
            for p in cart:
                amount += p.quantity*p.product.discount
            total_amount = amount+shipping_amount
            return render(request, 'app/addtocart.html', {'carts': cart, 'countCart': cart.count(), 'totalAmount': total_amount, 'amount': amount, 'shipping_amount': shipping_amount})
        else:
            return render(request, 'app/emptycart.html', {'countCart': 0})


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        product = Product.objects.get(id=prod_id)
        cart = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        cart.quantity += 1
        cart.save()
        list_cart = Cart.objects.filter(user=request.user)
        amount = 0.0
        shipping_amount = 5.0
        total_amount = 0.0
        for p in list_cart:
            amount += p.quantity*p.product.discount
            total_amount = amount+shipping_amount
            # return render(request, 'app/addtocart.html', {'carts': cart, 'countCart': cart.count(), 'totalAmount': total_amount, 'amount': amount, 'shipping_amount': shipping_amount})
        # else:
        #     return render(request, 'app/emptycart.html')
        data = {'totalAmount': total_amount,
                'amount': amount, 'quantity': cart.quantity}
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        product = Product.objects.get(id=prod_id)
        cart = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        cart.quantity -= 1
        cart.save()
        list_cart = Cart.objects.filter(user=request.user)
        amount = 0.0
        shipping_amount = 5.0
        total_amount = 0.0
        for p in list_cart:
            amount += p.quantity*p.product.discount
            total_amount = amount+shipping_amount
            # return render(request, 'app/addtocart.html', {'carts': cart, 'countCart': cart.count(), 'totalAmount': total_amount, 'amount': amount, 'shipping_amount': shipping_amount})
        # else:
        #     return render(request, 'app/emptycart.html')
        data = {'totalAmount': total_amount,
                'amount': amount, 'quantity': cart.quantity}
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        product = Product.objects.get(id=prod_id)
        cart = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        cart.delete()
        list_cart = Cart.objects.filter(user=request.user)
        amount = 0.0
        shipping_amount = 5.0
        total_amount = 0.0
        for p in list_cart:
            amount += p.quantity*p.product.discount
            total_amount = amount+shipping_amount
            # return render(request, 'app/addtocart.html', {'carts': cart, 'countCart': cart.count(), 'totalAmount': total_amount, 'amount': amount, 'shipping_amount': shipping_amount})
        # else:
        #     return render(request, 'app/emptycart.html')
        data = {'totalAmount': total_amount,
                'amount': amount}
        return JsonResponse(data)


def buy_now(request):
    return render(request, 'app/buynow.html')


# def profile(request):
#     return render(request, 'app/profile.html')

@login_required
def address(request):
    countCart = 0
    if request.user.is_authenticated:
        countCart = len(Cart.objects.filter(user=request.user))
    addresses = Customer.objects.filter(user=request.user)
    number = addresses[0].id
    return render(request, 'app/address.html', {'addresses': addresses, 'countCart': countCart, 'number': number-1})


@login_required
def orders(request):
    countCart = 0
    if request.user.is_authenticated:
        countCart = len(Cart.objects.filter(user=request.user))
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'Order_Placed': op, 'countCart': countCart})


# def change_password(request):
#     return render(request, 'app/changepassword.html')


def product_nugioi(request, data=None):
    if data == None:
        products = Product.objects.filter(category='san pham nu')
    elif data == 'F-1' or data == 'F-2' or data == 'F-3':
        products = Product.objects.filter(
            category='san pham nu').filter(brand=data)
    return render(request, 'app/mobile.html', {'products': products})


# def login(request):
#     return render(request, 'app/login.html')


class CustomerRegistrationView(View):
    def get(self, request):
        countCart = 0
        if request.user.is_authenticated:
            countCart = len(Cart.objects.filter(user=request.user))
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form, 'countCart': countCart})

    def post(self, request):
        countCart = 0
        if request.user.is_authenticated:
            countCart = len(Cart.objects.filter(user=request.user))
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Successfully')
            form.save()  # {'form': CustomerRegistrationForm()}
            return render(request, 'app/login.html', {'form': LoginForm(), 'countCart': countCart})
        return render(request, 'app/customerregistration.html', {'form': form, 'countCart': countCart})

# def customerregistration(request):
#     return render(request, 'app/customerregistration.html')


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        countCart = 0
        if request.user.is_authenticated:
            countCart = len(Cart.objects.filter(user=request.user))
        form = CustomerProfileForm
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary', 'countCart': countCart})

    def post(self, request):
        countCart = 0
        if request.user.is_authenticated:
            countCart = len(Cart.objects.filter(user=request.user))
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            address = form.cleaned_data['address']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            reg = Customer(user=user, name=name, mobile=mobile,
                           address=address, zipcode=zipcode, state=state)
            reg.save()
            messages.success(request, 'Update Profile successfully!')
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary', 'countCart': countCart})


@login_required
def checkout(request):
    countCart = 0
    if request.user.is_authenticated:
        countCart = len(Cart.objects.filter(user=request.user))
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 5.0
    total_amount = 0.0
    if cart_items.count():
        for p in cart_items:
            amount += p.quantity*p.product.discount
        total_amount = amount+shipping_amount
    return render(request, 'app/checkout.html', {'add': add, 'cart_items': cart_items, 'totalAmount': total_amount, 'amount': amount, 'shipping_amount': shipping_amount, 'countCart': countCart})


@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer,
                    product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect('orders')
