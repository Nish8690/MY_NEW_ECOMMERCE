from django.urls import path

from . import views

urlpatterns = [
    path("", views.lacritz, name="ShopLacritz"),
    path("home/", views.home, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    # path("shop/cart/", views.cartdetail, name="AboutUs"),
    path("contact", views.contact, name="ContactUs"),
    path("tracker", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("shop/products/<int:myid>", views.productView, name="ProductView"),
    path("checkout", views.checkout, name="Checkout"),
    path("shop/handlerequest/", views.handlerequest, name="HandleRequest"),
    path("logout/", views.handleLogout, name='handleLogout'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),

]
