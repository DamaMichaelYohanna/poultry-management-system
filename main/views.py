from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView
from django.contrib import messages


from .models import Farm, Store, Item
from .forms import PickOutForm


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


def sell_product(request):
    pass


def invoice(request):
    pass
