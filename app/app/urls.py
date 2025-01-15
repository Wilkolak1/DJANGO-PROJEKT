from django.urls import path
from app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("logowanie", views.signin, name="signin"),
    path("rejestracja", views.signup, name="signup"),
    path("wyloguj", views.signout, name="signout"),
    path("samochody", views.cars, name="cars"),
    path("obraz/<id>", views.car_image, name="car_image"),
    path("kontakt", views.contact, name="contact"),
    path("zamowienie/<id>", views.order, name="order"),
]
