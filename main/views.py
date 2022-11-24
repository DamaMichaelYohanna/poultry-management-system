from django.shortcuts import render
from .models import Farm


def index(request):
    # total_user = U
    return render(request, "index.html")


def store(request):
    pass


def farm_detail(request):
    detail = Farm.objects.get(id=1)
    return render(request, 'farm.html', {'farm': detail})


def sell_product(request):
    pass


def invoice(request):
    pass
