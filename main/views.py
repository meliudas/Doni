from django.shortcuts import render


def index(request):
    return render(request, 'index.html',)


def product(request):
    return render(request, 'product.html',)


def service(request):
    return render(request, 'service.html',)


def work(request):
    return render(request, 'work.html',)


def price(request):
    return render(request, 'price.html',)


def contact(request):
    return render(request, 'contact.html',)


def catalog(request):
    return render(request, 'catalog.html',)


def banner(request):
    return render(request, 'banner.html',)


def head(request):
    return render(request, 'head.html',)