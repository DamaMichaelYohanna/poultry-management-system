from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView
from django.contrib import messages

from .models import Farm, Store, Item, Product, Category, Order
from .forms import RestockForm


def index(request):
    # total_user = U
    return render(request, "index.html")


class StoreView(ListView):
    model = Store
    template_name = 'store.html'
    paginate_by = 6
    context_object_name = 'stock'


def add_to_store_item(request):
    """view to add to stock item in store"""
    if request.method == 'POST':
        name = request.POST.get('item')
        desc = request.POST.get('description')
        if name and desc:
            Item.objects.create(name=name, description=desc)
            print("done")
            messages.success(request, "Item added successfully")

        return redirect(reverse("main:store"))
    else:
        pass
    context = {}
    return render(request, 'restock.html', context)


def restock(request):
    if request.method == 'POST':
        restock_form = RestockForm(request.POST)
        if restock_form.is_valid():
            restock_form.save()
            return redirect(reverse('main:store'))
    else:
        restock_form = RestockForm()
    context = {'form': restock_form}
    print(context)
    return render(request, 'restock.html', context)


def pick_out(request, pk):
    item = Store.objects.get(pk=pk)
    if request.method == 'POST':
        post_item = request.POST.get('item')
        post_quantity = request.POST.get('quantity')
        if post_item and post_quantity:
            item.quantity -= int(post_quantity)
            item.save()
            if item.quantity == 0:
                del item
            else:
                item.save()
            return redirect(reverse("main:store"))
        else:
            print(post_item, post_quantity)
            print("something went wrong")

    else:
        pass
    context = {'item': item.item, 'quantity': item.quantity}
    return render(request, 'pickout.html', context)


def farm_detail(request):
    detail = Farm.objects.get(id=1)
    return render(request, 'farm.html', {'farm': detail})


def product_dashboard(request):
    product = Product.objects.all()
    category = Category.objects.all()
    try:
        cart = Order.objects.all()[0].product.all()
    except AttributeError:
        cart = None
    context = {'products': product, 'category': category, 'order': cart}
    return render(request, 'shopping.html', context)


def add_to_cart(request, pk):
    product = Product.objects.get(pk=pk)
    order = Order.objects.all()[0]
    if product not in order.product.all():
        order.product.add(product)
        order.save()
    messages.success(request, 'added to cart successfully')
    return redirect(reverse('main:product_dashboard'))


def remove_from_cart(request, pk):
    product = Product.objects.get(pk=pk)
    order = Order.objects.all()[0]
    if product in order.product.all():
        order.product.remove(product)
        order.save()

    messages.success(request, 'removed from cart successfully')
    return redirect(reverse('main:product_dashboard'))


def checkout(request):
    order = Order.objects.all()[0]
    if request.method == 'POST':
        pass
    else:
        pass
    context = {'order': order.product.all()}
    return render(request, 'checkout.html', context)


def product_add(request):
    return render(request, 'product_')


def product_update(request):
    return render(request, 'product_')


def product_delete(request):
    return render(request, 'product_')


def invoice(request):
    pass
