from django.shortcuts import render
from .models import Farm, Store


def index(request):
    # total_user = U
    return render(request, "index.html")


def store(request):
    item = Store.objects.all()
    context = {'stock': item}
    return render(request, 'store.html', context)


def farm_detail(request):
    detail = Farm.objects.get(id=1)
    return render(request, 'farm.html', {'farm': detail})


def sell_product(request):
    pass


def invoice(request):
    pass
