import datetime

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages

from .models import Farm, Store, Item, Order, InvoiceProduct, Invoice, GProduct, GProductCategory
from .forms import RestockForm, GProductForm, GProductCategoryForm
from .utility import generate_ref


def index(request):

    def calculate_sum(obj):
        sale_sum = 0
        for rec in obj:
            sale_sum += rec.price
        return sale_sum

    total_user = User.objects.all().count()
    total_product = GProduct.objects.all().count()
    store_product = Store.objects.all().count()
    sale_rec = InvoiceProduct.objects.all()
    today_sales_rec = sale_rec.filter(date=datetime.datetime.now().date())
    yesterday_sales_rec = sale_rec.filter(
        date=datetime.datetime.now().date() - datetime.timedelta(days=1)
    )
    # --------------------------------------
    total_sales_sum = calculate_sum(sale_rec)  # calculate total sales ever made
    today_sales_sum = calculate_sum(today_sales_rec)  # calculate sales for today
    yesterday_sales_sum = calculate_sum(yesterday_sales_rec)  # calculate sales for today

    context = {"user": total_user, 'total_sum': total_sales_sum,
               "today_sum": today_sales_sum, 'yesterday_sum': yesterday_sales_sum,
               'total_product': total_product, 'store': store_product}
    return render(request, "index.html", context)


def product_management(request):
    """view for listing product and adding new product"""
    if request.method == 'POST':
        form = GProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully.")
            return redirect(reverse("main:product_management"))
        else:
            print("forms is invalid")
            print(form)
    else:
        form = GProductForm()

    product = GProduct.objects.all()
    category = GProductCategory.objects.all()
    context = {'form': form, 'product': product, 'cat': category}

    return render(request, 'product_management.html', context)


def category_management(request):
    """view for listing product category and adding new product"""
    if request.method == 'POST':
        form = GProductCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "category added successfully.")
            return redirect(reverse("main:category_management"))
    else:
        form = GProductCategoryForm()
    product = GProductCategory.objects.all()
    context = {'form': form, 'category': product}
    return render(request, 'category_management.html', context)


def product_update(request, pk):
    product = get_object_or_404(GProduct, pk=pk)
    if request.method == 'POST':
        form = GProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully.")
            return redirect(reverse("main:product_management"))
        else:
            print("forms is invalid")
            print(form)
    else:
        form = GProductForm(instance=product)
    return render(request, 'product_update.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(GProduct, pk=pk)
    product.delete()
    return render(redirect(reverse('main:product_management')))


# ---------------------------------------------------------
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
    return render(request, 'farm.html', )


def product_dashboard(request):
    product = GProduct.objects.all()
    category = GProductCategory.objects.all()
    try:
        cart = Order.objects.all()[0].product.all()
    except AttributeError:
        cart = []
    except IndexError:
        cart = []
    context = {'products': product, 'category': category, 'order': cart}
    return render(request, 'shopping.html', context)


def add_to_cart(request, pk):
    product = GProduct.objects.get(pk=pk)
    try:
        order = Order.objects.all()[0]
    except IndexError:
        order = Order.objects.create()
        order.product.add(product)
        order.save()
    else:
        if product not in order.product.all():
            order.product.add(product)
            order.save()
    messages.success(request, 'added to cart successfully')
    return redirect(reverse('main:product_dashboard'))


def remove_from_cart(request, pk):
    product = GProduct.objects.get(pk=pk)
    order = Order.objects.all()[0]
    if product in order.product.all():
        order.product.remove(product)
        order.save()

    messages.success(request, 'removed from cart successfully')
    return redirect(reverse('main:product_dashboard'))


def clear_cart(request):
    Order.objects.all().delete()
    # del order
    return redirect(reverse('main:product_dashboard'))


def checkout(request):
    order = Order.objects.all()[0]
    total_price = 0
    for i in order.product.all():
        total_price += i.price
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        payment = request.POST.get('payment')
        ref_code = generate_ref()
        for item in order.product.all():
            if item.name in request.POST:
                InvoiceProduct.objects.create(name=item.name,
                                              quantity=request.POST.get(item.name),
                                              ref=ref_code, price=item.price)
            else:
                print("no item in request")
        purchase_item = InvoiceProduct.objects.filter(ref=ref_code)
        if purchase_item:
            obj = Invoice(ref=ref_code, customer=name, contact=contact, payment=payment)
            obj.save()
            obj.goods.add(*purchase_item)
            obj.save()
            messages.success(request, "Record saved successfully")
            order.delete()
            return redirect(f'/invoice/{ref_code}')

    else:
        pass
    context = {'order': order.product.all(), 'total': total_price}
    return render(request, 'checkout.html', context)


def single_invoice(request, ref):
    obj = Invoice.objects.get(ref=ref)
    context = {'obj': obj}
    return render(request, 'single_invoice.html', context)


def all_invoice(request):
    obj = Invoice.objects.all()
    context = {'invoices': obj}
    return render(request, 'invoices.html', context)
