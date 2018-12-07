from django.contrib import admin

# Register your models here.

from .models import Category, Topping, Size, PizzaType, Price, ToppingNumber, Food, OrderNumber, Order, ExtraSub


class FoodInline(admin.StackedInline):
    model = Food
    extra = 1
    fields = ["name"]


class SizeAdmin(admin.ModelAdmin):
    inlines = [FoodInline]


class CategoryAdmin(admin.ModelAdmin):
    inlines = [FoodInline]


class FoodAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "size", "type", "select_toppings", "price"]
    list_editable = ["price"]
    list_filter = ["category", "type", "size", "select_toppings"]
    save_as = True
    save_on_top = True
    search_fields = ["name"]


class OrderInline(admin.TabularInline):
    model = Order
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    # list_display = ["food"]
    model = Order
    filter_horizontal = ["toppings", "extra_sub",]
    # list_filter = [""]
    save_on_top = True


class OrderNumAdmin(admin.ModelAdmin):
    inlines = [OrderInline]
    list_display = ["username", "date", "total", "in_cart", "in_process", "done"]
    list_editable = ["in_cart", "in_process", "done"]
    list_filter = ["total", "in_cart", "in_process", "done", "username"]
    save_on_top = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Price)
admin.site.register(ExtraSub)
admin.site.register(ToppingNumber)
admin.site.register(PizzaType)
admin.site.register(Topping)
admin.site.register(Food, FoodAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderNumber, OrderNumAdmin)

