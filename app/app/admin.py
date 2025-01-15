from django.contrib import admin
from .models import Account, Car, Order, ContactMessage

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user__username', 'user__first_name', 'user__email', 'phone']

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'price_per_day']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['account__user__username', 'car__name', 'days_for_rent']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['message', 'is_read']
