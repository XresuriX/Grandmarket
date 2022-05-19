from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'market/home.html')


def market(request):
    return render(request, 'market/market.html')


def add(request):
    return render(request, 'market/add.html')


def cart(request):
    return render(request, 'market/cart.html')


def order(request):
    return render(request, 'market/order.html')


def detail(request):
    return render(request, 'market/page-detail.html')


def profile(request):
    return render(request, 'market/profile.html')


def signup(request):
    return render(request, 'market/sign-up.html')


def signin(request):
    return render(request, 'market/sign-in.html')


def store(request):
    return render(request, 'market/store_front.html')


def search(request):
    return render(request, 'market/search.html')


def stores(request):
    return render(request, 'market/stores.html')


def new_store(request):
    return render(request, 'market/storeform.html')


def favorites(request):
    return render(request, 'market/favorites.html')


def about(request):
    return render(request, 'market/about.html')
