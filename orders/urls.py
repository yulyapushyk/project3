from django.urls import path

from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.menu_pizza, name="menu_pizza"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("cart", views.cart, name="cart"),
    path("signup", views.signup, name="signup"),
    # path("menu_pizza", views.menu_pizza, name="menu_pizza"),
    path("menu_subs", views.menu_subs, name="menu_subs"),
    path("menu_pasta", views.menu_pasta, name="menu_pasta"),
    path("menu_salads", views.menu_salads, name="menu_salads"),
    path("menu_dinner_platters", views.menu_dinner_platters, name="menu_dinner_platters"),
    path("pizza/<int:pizza_id>", views.pizza, name="pizza"),
    path("<int:pizza_id>/pizza_order", views.pizza_order, name="pizza_order"),
    path("sub/<int:sub_id>", views.subs, name="subs"),
    path("<int:sub_id>/sub_order", views.sub_order, name="sub_order"),
    path("pasta/<int:pasta_id>", views.pasta, name="pasta"),
    path("<int:pasta_id>/pasta_order", views.pasta_order, name="pasta_order"),
    path("salads/<int:salad_id>", views.salads, name="salads"),
    path("<int:salad_id>/salads_order", views.salads_order, name="salads_order"),
    path("dinner_platters/<int:dinner_platter_id>", views.dinner_platters, name="dinner_platters"),
    path("<int:dinner_platters_id>/dinner_platters_order", views.dinner_platters_order, name="dinner_platters_order"),
    path("delete", views.delete, name="delete"),
    path("checkout", views.checkout, name="checkout"),
    path("orders", views.orders, name="orders"),
    path("send_email", views.send_email, name="send_email"),
    path("order", views.orders_done, name="order_done"),
]

