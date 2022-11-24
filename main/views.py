from django.shortcuts import render


def index(request):
    # total_user = U
    return render(request, "index.html")


def store(request):
    pass


def farm_detail(request):
    return render(request, 'farm.html')


def sell_product(request):
    pass


def invoice(request):
    pass
