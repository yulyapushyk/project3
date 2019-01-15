from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from .models import Food, Topping, OrderNumber, Order, ExtraSub
from django.urls import reverse
from django.db.models import ProtectedError
from django.core.mail import send_mail
from django.template.loader import render_to_string


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("menu_pizza"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials."})
    else:
        return render(request, "orders/login.html", {"message": ""})


def logout_view(request):
    logout(request)
    return redirect('menu_pizza')


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('menu_pizza')
    else:
        form = RegisterForm()
    return render(request, 'orders/signup.html', {'form': form})


def cart1(username, email):
    try:
        cart1 = OrderNumber.objects.get(username=username, in_cart=True)
    except OrderNumber.DoesNotExist:
        total_0 = OrderNumber.objects.filter(total=0)
        if total_0:
            total_0.delete()
        cart1 = OrderNumber(username=username, email=email)
        cart1.save()
    return cart1


def total(order):
    if not isinstance(order, OrderNumber):
        raise Http404("{} is not an instance of OrderNumber.".format(order))
    else:
        items = order.order_items.all()
        order.total = 0
        for item in items:
            order.total += item.price * int(item.quantity)
        order.save()


def cart_count(username):
    try:
        cart1 = OrderNumber.objects.get(username=username, in_cart=True)
    except OrderNumber.MultipleObjectsReturned:
        raise Http404("More than one cart found.")
    except OrderNumber.DoesNotExist:
        return 0
    else:
        return cart1.order_items.exclude(extra=True).count()


def menu_pizza(request):
    username = request.user.username

    context = {
        "toppings": Topping.objects.all(),
        "regular_pizza_small": Food.objects.filter(category__name__icontains="Pizza").
            filter(type__type__icontains="Regular").filter(size__size__icontains="Small"),
        "regular_pizza_large": Food.objects.filter(category__name__icontains="Pizza").
            filter(type__type__icontains="Regular").filter(size__size__icontains="Large"),
        "sicilian_pizza_small": Food.objects.filter(category__name__icontains="Pizza").
            filter(type__type__icontains="Sicilian").filter(size__size__icontains="Small"),
        "sicilian_pizza_large": Food.objects.filter(category__name__icontains="Pizza").
            filter(type__type__icontains="Sicilian").filter(size__size__icontains="Large"),
        "cart_count": cart_count(username)
    }

    return render(request, "orders/menu_pizza.html", context)


def menu_subs(request):
    username = request.user.username
    context = {
        "subs_small": Food.objects.filter(category__name__icontains="Subs").
            filter(size__size__icontains="Small").exclude(extra="True"),
        "subs_large": Food.objects.filter(category__name__icontains="Subs").
            filter(size__size__icontains="Large").exclude(extra="True"),
        "cart_count": cart_count(username)
    }
    return render(request, "orders/menu_subs.html", context)


def menu_pasta(request):
    username = request.user.username
    context = {
        "pasta": Food.objects.filter(category__name__icontains="Pasta"),
        "cart_count": cart_count(username),
    }


    return render(request, "orders/menu_pasta.html", context)


def menu_salads(request):
    username = request.user.username
    context = {
        "salads": Food.objects.filter(category__name__icontains="Salads"),
        "cart_count": cart_count(username)
    }
    # if request.method == 'POST':
    #     username = request.user.username
    #     email = request.user.email
    #     order = cart1(username, email)
    #     salad_id = request.POST.get('salad' + str(n), False)
    #     salad_id = int(request.POST['{{ salads.id }}'])
    #     print(salad_id)
    #     salad = Food.objects.filter(category__name__icontains="Salads").get(pk=salad_id)
    #     number = int(request.POST['number'])
    #     O = Order(order_num=order, username=username, food=salad, quantity=number, total_price=number * salad.price,
    #               price=salad.price)
    #     O.save()
    #     total(order)
    return render(request, "orders/menu_salads.html", context)


def menu_dinner_platters(request):
    username = request.user.username
    context = {
        "dinner_platters_small": Food.objects.filter(category__name__icontains="Dinner Platters").
            filter(size__size__icontains="Small"),
        "dinner_platters_large": Food.objects.filter(category__name__icontains="Dinner Platters").
            filter(size__size__icontains="Large"),
        "cart_count": cart_count(username)
    }
    return render(request, "orders/menu_dinner_platters.html", context)


def pizza(request, pizza_id):
    username = request.user.username
    if not username:
        return redirect('login')
    toppings = Topping.objects.all()
    pizza_list = Food.objects.filter(category__name__icontains="Pizza").all()
    pizza = Food.objects.filter(category__name__icontains="Pizza").get(pk=pizza_id)
    return render(request, "orders/pizza.html", {'pizza_list': pizza_list, 'pizza': pizza,  'toppings': toppings, 'cart_count': cart_count(username)})


def subs(request, sub_id):
    username = request.user.username
    if not username:
        return redirect('login')
    subs_list = Food.objects.filter(category__name__icontains="Subs").all()
    sub = Food.objects.filter(category__name__icontains="Subs").get(pk=sub_id)
    extra_sub = ExtraSub.objects.all()
    return render(request, "orders/subs.html", {'subs_list': subs_list, 'sub': sub, 'extra_sub': extra_sub, 'cart_count': cart_count(username)})


def pasta(request, pasta_id):
    username = request.user.username
    if not username:
        return redirect('login')
    pasta_list = Food.objects.filter(category__name__icontains="Pasta").all()
    pasta = Food.objects.filter(category__name__icontains="Pasta").get(pk=pasta_id)
    return render(request, "orders/pasta.html", {'pasta_list': pasta_list, 'pasta': pasta, 'cart_count': cart_count(username)})


def salads(request, salad_id):
    username = request.user.username
    if not username:
        return redirect('login')
    salad_list = Food.objects.filter(category__name__icontains="Salads").all()
    salad = Food.objects.filter(category__name__icontains="Salads").get(pk=salad_id)
    return render(request, "orders/salads.html", {'salad_list': salad_list, 'salad': salad, 'cart_count': cart_count(username)})


def dinner_platters(request, dinner_platter_id):
    username = request.user.username
    if not username:
        return redirect('login')
    dinner_platters_list = Food.objects.filter(category__name__icontains="Dinner Platters").all()
    dinner_platter = Food.objects.filter(category__name__icontains="Dinner Platters").get(pk=dinner_platter_id)
    return render(request, "orders/dinner_platters.html", {'dinner_platters_list': dinner_platters_list,
                                                           'dinner_platter': dinner_platter, 'cart_count': cart_count(username)})


def pizza_order(request, pizza_id):
    pizza = Food.objects.filter(category__name__icontains="Pizza").get(pk=pizza_id)
    pizza_price = pizza.price.price
    if request.method == 'POST':
        username = request.user.username
        email = request.user.email
        order = cart1(username, email)
        pizza.save()
        number = int(request.POST['number'])
        O = Order(order_num=order, username=username, food=pizza, quantity=number, total_price=number * pizza_price,
                  price=pizza_price)
        O.save()
        total(order)
        if pizza.select_toppings.number == "Special":
            num = 4
        elif pizza.select_toppings.number == "3 toppings":
            num = 3
        elif pizza.select_toppings.number == "2 toppings":
            num = 2
        elif pizza.select_toppings.number == "1 topping":
            num = 1
        elif pizza.select_toppings.number == "Cheese":
            num = 0
        if num == 0:
            topping = "None"
        for n in range(1, num+1):
            toppingname = request.POST.get('topping' + str(n))
            topping = Topping.objects.get(name=toppingname)
            if toppingname:
                try:
                    topping = Topping.objects.get(
                        name=toppingname
                    )
                except Topping.DoesNotExist:
                    raise Http404("""No such topping""")
                else:
                    O.toppings.add(topping)
                    pizza.save()
                    total(order)
    return HttpResponseRedirect(reverse("menu_pizza"), {'topping': topping})


def sub_order(request, sub_id):
    sub = Food.objects.filter(category__name__icontains="Subs").get(pk=sub_id)
    sub_price = sub.price.price
    if request.method == 'POST':
        username = request.user.username
        email = request.user.email
        order = cart1(username, email)
        sub.save()
        number = int(request.POST['number'])
        O = Order(order_num=order, username=username, food=sub, quantity=number, total_price=number * sub_price,
                  price=sub_price)
        O.save()
        total(order)
        for n in range(5):
            extra_sub = request.POST.get('extra' + str(n), False)
            if extra_sub:
                try:
                    itemextra = ExtraSub.objects.get(name=extra_sub)
                    extra = Food.objects.get(
                        name=itemextra
                    )
                except ExtraSub.DoesNotExist:
                    raise Http404("Can't find extra sub.")
                else:
                    O.extra_sub.add(itemextra)
                    extra_price = extra.price.price
                    sub_extra = Order(order_num=order, username=username, quantity=number, food=extra,
                                      price=extra.price.price, total_price=number * extra_price,
                                      extra=True)
                    sub_extra.save()
                    total(order)
    return HttpResponseRedirect(reverse("menu_subs"), {'number': number})


def pasta_order(request, pasta_id):
    pasta = Food.objects.filter(category__name__icontains="Pasta").get(pk=pasta_id)
    pasta_price = pasta.price.price
    if request.method == 'POST':
        username = request.user.username
        email = request.user.email
        order = cart1(username, email)
        pasta.save()
        number = int(request.POST['number'])
        O = Order(order_num=order, username=username, food=pasta, quantity=number, total_price=number * pasta_price,
                  price=pasta_price)
        O.save()
        total(order)
    return HttpResponseRedirect(reverse("menu_pasta"))


def salads_order(request, salad_id):
    salad = Food.objects.filter(category__name__icontains="Salads").get(pk=salad_id)
    salad_price = salad.price.price
    if request.method == 'POST':
        username = request.user.username
        email = request.user.email
        order = cart1(username, email)
        salad.save()
        number = int(request.POST['number'])
        O = Order(order_num=order, username=username, food=salad, quantity=number, total_price=number * salad_price,
                  price=salad_price)
        O.save()
        total(order)
    return HttpResponseRedirect(reverse("menu_salads"))


def dinner_platters_order(request, dinner_platters_id):
    dinner_platter = Food.objects.filter(category__name__icontains="Dinner Platters").get(pk=dinner_platters_id)
    dinner_platter_price = dinner_platter.price.price
    if request.method == 'POST':
        username = request.user.username
        email = request.user.email
        order = cart1(username, email)
        dinner_platter.save()
        number = int(request.POST['number'])
        O = Order(order_num=order, username=username, food=dinner_platter, quantity=number, total_price=number * dinner_platter_price,
                  price=dinner_platter_price)
        O.save()
        total(order)
    return HttpResponseRedirect(reverse("menu_dinner_platters"))


def cart(request):
    username = request.user.username
    email = request.user.email
    if not username:
        return redirect('login')
    order = cart1(username, email)
    cart = order.order_items.all()
    for item in cart:
        total_food = int(item.quantity) * item.price
        print(total_food)
    extra = order.order_items.all().filter(extra=True)
    print(extra)
    total = order.total
    return render(request, 'orders/cart.html', {'cart': cart, 'cart_count': cart_count(username),
                                                'total': total, 'order': order, })


def checkout(request):
    username = request.user
    if not username:
        return redirect('login')
    try:
        cart = OrderNumber.objects.get(username=username, in_cart=True)
    except OrderNumber.MultipleObjectsReturned:
        raise Http404("More than one cart found.")
    except OrderNumber.DoesNotExist:
        raise Http404("No cart exists.")
    else:
        cart.in_cart = False
        cart.in_process = True
        cart.save()
    cart = cart.order_items.all()
    context = {
        "order_number": OrderNumber.objects.all()[0],
        "cart_count": cart_count(username),
        "username": username,
    }
    email = request.user.email
    msg_html = render_to_string('orders/email.html', {'username': username, 'cart': cart})
    data = """
    {} {}, thanks for your order.
    We are working on it.
    Here is detail information about your order http://127.0.0.1:8000/orders. 
    
    Pinocchio's Pizza & Subs
    74 Winthrop Street Harvard Square
    617-876-4897
    pinnocciopizza@gmail.com
        """.format(username.first_name, username.last_name)
    send_mail(
        '{}, your order is accepted'.format(username.first_name.capitalize()),
        data,
        'pinnocciopizza@gmail.com',
        [email],
        fail_silently=False,
        html_message=msg_html,
    )
    return render(request, 'orders/checkout.html', context)


def orders(request):
    username = request.user.username
    email = request.user.email
    if not username:
        return redirect('login')
    orders_user = OrderNumber.objects.filter(in_cart=False, in_process=True, done=False, username=username)|\
             OrderNumber.objects.filter(in_cart=False, in_process=False, done=True, username=username)|\
             OrderNumber.objects.filter(in_cart=False, in_process=True, done=True, username=username).order_by("-date")
    orders = OrderNumber.objects.filter(in_cart=False, in_process=True, done=False)|\
             OrderNumber.objects.filter(in_cart=False, in_process=False, done=True)|\
             OrderNumber.objects.filter(in_cart=False, in_process=True, done=True, username=username).order_by("-date")
    order = cart1(username, email)
    context = {
        'orders': orders,
        'orders_user': orders_user,
        'total': total(order),
        'cart_count': cart_count(username),
        'username': username,
    }
    return render(request, 'orders/order.html', context)


def delete(request):
    username = request.user.username
    email = request.user.email
    try:
        id = request.POST['order_id']
        Order.objects.get(id=int(id), username=username).delete()
        order = cart1(username, email)
        total(order)
    except ProtectedError:
        raise Http404('Can not remove order object.')
    except Order.DoesNotExist:
        raise Http404('Order does not exist.')
    return redirect("cart")


def orders_done(request):
    username = request.user.username
    email = request.user.email
    orders = OrderNumber.objects.filter(in_process=True, done=False).exclude(total=0).order_by("-date")
    order = cart1(username, email)
    context = {
        'orders': orders,
        'total': total(order),
    }
    return render(request, 'orders/orders.html', context)


def send_email(request):
    username = request.user
    try:
        id = request.POST['order_id']
        order = OrderNumber.objects.get(id=int(id))
        order.in_cart = False
        order.in_process = False
        order.done = True
        order.save()
    except OrderNumber.DoesNotExist:
        raise Http404('Order does not exist.')
    email = order.email
    data = """
        {}, thanks for your order #{} on {}$.
        It is completed and sent to you.
        You will soon get it. 
        Here is detail information about your order https://yulya-project3.herokuapp.com/orders.
        Bon appetite!

        Pinocchio's Pizza & Subs
        74 Winthrop Street Harvard Square
        617-876-4897
        pinnocciopizza@gmail.com
        
            """.format(order.username.capitalize(), order.id, order.total)
    try:
        cart_done = OrderNumber.objects.filter(done=True)
    except OrderNumber.DoesNotExist:
        raise Http404("No cart exists.")
    else:
        if cart_done:
            send_mail(
                '{}, your order is on way to you'.format(order.username.capitalize()),
                data,
                'pinnocciopizza@gmail.com',
                [email],
                fail_silently=False,
            )
    return redirect("order_done")


