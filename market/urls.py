from django.urls import path
from . import views


app_name = 'market'
urlpatterns = [
    path('', views.home, name='home'),
    path('Grandmarket/market', views.market, name='market'),
    path('Grandmarket/add-item', views.add, name='add-item'),
    path('Grandmarket/cart', views.cart, name='cart'),
    path('Grandmarket/order', views.order, name='orders'),
    path('Grandmarket/detail', views.detail, name='detail'),
    path('Grandmarket/profile', views.profile, name='profile'),
    path('Grandmarket/store', views.store, name='store'),
    path('Grandmarket/search', views.search, name='search results'),
    path('Grandmarket/stores', views.stores, name='stores'),
    path('Grandmarket/sign-in', views.signin, name='sign-in'),
    path('Grandmarket/sign-up', views.signup, name='sign-up'),
    path('Grandmarket/favorites', views.favorites, name='favorites'),
    path('Grandmarket/about', views.about, name='about'),
]
