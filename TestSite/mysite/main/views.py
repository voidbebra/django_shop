import json
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.views.decorators.http import require_POST

from .cart import Cart
from .forms import CartAddProductForm, CreateUserForm
from .models import Prod

def maine(request):
    last_id = Prod.objects.latest('id').id
    latest_products = [Prod.objects.get(id=last_id)]
    latest_products += [Prod.objects.get(id=last_id-1)]
    context = {
        'latest_products': latest_products
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')

def products(request):
    products = Prod.objects.all() 

    context = {'products': products}

    return render(request, 'main/products.html', context)

@login_required(login_url='login')
def get_user_list(request):
    from django.contrib.auth.models import User

    users = User.objects.all()
    context = {'users': users}

    return render(request, 'main/users_list.html', context)


def dj_register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {
        'form': form,
        'form_name': 'Register Account',
        'info_text': 'Already have an account?',
        'info_url': 'login',
        'info_btn_text': 'Sign in'
    }
    return render(request, 'main/register.html', context)


def dj_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')

    context = {
        'form_name': 'Login',
        'info_text': 'Don\'t have an account?',
        'info_url': 'register',
        'info_btn_text': 'Sign up'
    }
    return render(request, 'main/login.html', context)


def dj_logout(request):
    logout(request)
    return redirect('home')

def product_detail(request, id):
    product = get_object_or_404(Prod, id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'main/detail.html', {'product': product, 'cart_product_form':cart_product_form})

@require_POST
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Prod, id=id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])

        response = {'data':cart.cart}
        
        return JsonResponse({'success':True, 'data':response})
    else: 
        return JsonResponse({'success':False, 'errors':"я хз"})


def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Prod, id=id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'main/cart_detail.html', {'cart': cart})