from django.shortcuts import render
from django.views.generic import ListView
from .models import Farm, Store


def index(request):
    # total_user = U
    return render(request, "index.html")


class Store(ListView):
    model = Store
    template_name = 'store.html'
    paginate_by = 10
    context_object_name = 'stock'


def farm_detail(request):
    detail = Farm.objects.get(id=1)
    return render(request, 'farm.html', {'farm': detail})


def sell_product(request):
    pass


def invoice(request):
    pass
