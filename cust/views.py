from django.shortcuts import redirect, render
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

# deco
from django.contrib.auth.decorators import login_required
from cust.decoratorsFile import user_is_authenticated, allowed_user, admin_only

# messages
from django.contrib import messages

# create your views here
from .models import *
from .forms import OrderForm, CreateUserForms
from .filters import OrderFilter



# login form
# id is 'henil' and passwor is 'shah@123'
@user_is_authenticated
def loginForm(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('cust_home')
        else:
            messages.info(request, 'username and password is incorrect')
    return render(request, 'accounts/loginForm.html')

# logout
def logout_user(request):
    logout(request)
    return redirect('loginForm')

# Regression form
@user_is_authenticated
def registrationForm(request):
    form = CreateUserForms()
    if request.method == "POST":
        form = CreateUserForms(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            # this query is automatically set the user as a customer
            group = Group.objects.get(name = 'customer')
            user.groups.add(group)


            messages.success(request, 'Account was created for\t' + username)

            return redirect('loginForm')   
    return render(request, 'accounts/registrationForm.html', {'form':form})


# Create your views here.

@login_required(login_url='loginForm')
@admin_only
# you can add many rols
# @allowed_user(allowed_rolls=['admin', 'staff'])
def cust_home(request):
    custm = Customer.objects.all()
    prod = Order.objects.all()

    # total order
    total_order = Order.objects.all().count()
    Delivered = Order.objects.filter(status = 'delivery').count()
    Pending = Order.objects.filter(status = 'pending').count()

    data = {
        'cust' : custm,
        'prob':prod,
        'total_order': total_order,
        'Delivered' : Delivered,
        'Pending' : Pending
    }

    return render(request,'accounts/dashboard.html', data)


# cust_products table 
@login_required(login_url='loginForm')
@allowed_user(allowed_rolls=['admin'])
def cust_products(request):
    temp = Product.objects.all()
    data = {
        'all_info' : temp
    }
    return render(request, 'accounts/products.html', data)

# customer
@login_required(login_url='loginForm')
@allowed_user(allowed_rolls=['admin'])
def customer(request, id):
    customer_id = Customer.objects.get(id = id)
    orders = customer_id.order_set.all()
    ord_count = orders.count()
    
    MyFilter = OrderFilter(request.GET, queryset=orders)
    orders = MyFilter.qs


    
    params = {
        'customer_id': customer_id,
        'ord':orders,
        'data':ord_count,
        'MyFilter':MyFilter
    }
    return render(request, "accounts/customer.html", params)

# create order
@login_required(login_url='loginForm')
@allowed_user(allowed_rolls=['admin'])
def order_product(request, id):
    OrderFromsSet = inlineformset_factory(Customer, Order, fields=('Product', 'status'))
    customer = Customer.objects.get(id = id)
    formset = OrderFromsSet(queryset=Order.objects.none() ,instance =customer)
    # forms = OrderForm(initial={'customer':customer})
    # print(f'\n\n\n{forms}\n\n\n')
    if request.method == 'POST':
        # print('\nprinting data\n',request.POST) 
        # form = OrderForm(request.POST)
        formset =OrderFromsSet(request.POST, instance = customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    return render(request, 'accounts/create_ord.html', {'formset':formset})

# dash update order
@login_required(login_url='loginForm')
@allowed_user(allowed_rolls=['admin'])
def updateOrder(request, id):
    order_update_data = Order.objects.get(id = id)  
    forms = OrderForm(instance=order_update_data)
    # print(f'print\n{forms}')
    if request.method == 'POST':
        # print('\nprinting data\n',request.POST) 
        form = OrderForm(request.POST, instance=order_update_data)
        if form.is_valid():
            print("\nif part is working\n")
            # form.save()
            return redirect('/')
    return render(request, 'accounts/update_order.html', {'form':forms})


# dbcustomer
@login_required(login_url='loginForm')
@allowed_user(allowed_rolls=['admin'])
def dbcustomer(request):
    data = Customer.objects.all()
    return render(request, "accounts/db_table/db_cust.html", {'data':data})

# dborder
@login_required(login_url='loginForm')
@allowed_user(allowed_rolls=['admin'])
def dborder(request): 
    data = Order.objects.all()
    return render(request, "accounts/db_table/db_ord.html", {'data':data})

# dbproduct
@login_required(login_url='loginForm')
@allowed_user(allowed_rolls=['admin'])
def dbproduct(request):
    data = Product.objects.all()
    return render(request, "accounts/db_table/db_prod.html", {'data':data})



# user page
def userpage(request):
    return render(request, 'accounts/users.html')




# dashboard delete order
@login_required(login_url='loginForm')
@allowed_user(allowed_rolls=['admin'])
def deteleOrder(request, id):
    order_data = Order.objects.get(id = id)
    if request.method == 'POST':
        order_data.delete()
        return redirect('/')

    return render(request,'accounts/delete_data.html', {'order_data':order_data})

