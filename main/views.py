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
    print(item.item)
    print(item.quantity)
    if request.method == 'POST':
        pick_out_form = PickOutForm(request.POST)
        if pick_out_form.is_valid():
            print(pick_out_form.cleaned_data)
            print("form is clean")
        else:
            print("form is invalid")
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
