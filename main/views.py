from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView
from django.contrib import messages
from .models import Farm, Store, Item


def index(request):
    # total_user = U
    return render(request, "index.html")


class Store(ListView):
    model = Store
    template_name = 'store.html'
    paginate_by = 6
    context_object_name = 'stock'


def add_to_store_item(request):
    if request.method == 'POST':
        name = request.POST.get('item')
        desc = request.POST.get('description')
        if name and desc:
            Item.objects.create(name=name, description=desc)
            print("done")
            messages.success(request, "Item added successfully")

    return redirect(reverse("main:store"))


def pick_out(request):
    return render(request, 'pickout.html')


def farm_detail(request):
    detail = Farm.objects.get(id=1)
    return render(request, 'farm.html', {'farm': detail})


def sell_product(request):
    pass


def invoice(request):
    pass
