from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account, ContactMessage, Car, Order
from django.contrib.auth import login, authenticate, logout
from django.http import FileResponse
import datetime
from .forms import SignInForm, SignUpForm, ContactForm, OrderForm

def require_login(view):
    def wrapper(*args, **kwargs):
        request = args[0]
        if request.user.is_authenticated: return view(*args, **kwargs)
        else: return redirect('signin')
    return wrapper

def home(request):
    return render(request, 'home.html', {})

def signin(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user:
                login(request, user)
                return redirect('home')
        return render(request, 'signin.html', {'form': form, 'bad_data': True})
    return render(request, 'signin.html', {'form': SignInForm()})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        errors = []
        if not form.is_valid(): errors.append("Formularz jest nie poprawny!")
        if User.objects.filter(username=form.cleaned_data.get('username')).exists(): errors.append("Użytkownik z taką nazwą już istnieje!")
        if form.cleaned_data.get('password2') != form.cleaned_data.get('password1'): errors.append("Hasła są różne!")
        if len(errors) == 0:
            user = User(
                username=form.cleaned_data.get('username'), 
                password=form.cleaned_data.get('password1'), 
                first_name=form.cleaned_data.get('first_name'), 
                last_name=form.cleaned_data.get('last_name')
            )
            user.save()
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            account = Account(address=form.cleaned_data.get('address'), phone=form.cleaned_data.get('phone'), user=user)
            account.save()
            return redirect('signin')
        else:
            return render(request, 'signup.html', {'errors': errors, 'form': form})
    else:
        return render(request, 'signup.html', {'errors': [], 'form': SignUpForm()})

def signout(request):
    logout(request)
    return redirect('home')

@require_login
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data.get('message')
            account = Account.get_by_user_id(request.user.id)
            contact_message = ContactMessage(message=message, account=account)
            contact_message.save()
            return render(request, 'contact.html', {'sent': True, 'form': ContactForm()})
    return render(request, 'contact.html', {'form': ContactForm()})

@require_login
def cars(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', {'cars': cars})

@require_login
def order(request, id):
    car = Car.objects.filter(id=id).first()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get('date')
            account = Account.get_by_user_id(request.user.id)
            days_for_rent = form.cleaned_data.get('days')
            Order(account=account, date=date, days_for_rent=days_for_rent, car=car).save()
            return render(request, 'order.html', {'car': car, 'done': True, 'form': OrderForm()})
        else:
            return render(request, 'order.html', {'car': car, 'form': form})
    return render(request, 'order.html', {'car': car, 'form': OrderForm()})

@require_login
def car_image(request, id):
    car = Car.objects.filter(id=id).first()
    return FileResponse(open(car.image.path, 'rb'))
