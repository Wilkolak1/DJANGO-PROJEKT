from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone = models.CharField(max_length=16)

    @staticmethod
    def get_by_user_id(id):
        return Account.objects.filter(user=User.objects.filter(id=id).first()).first()
    
    def __str__(self):
        return self.user.username

def get_car_image_path(instance, filename):
        ext = filename.split('.')[-1]
        return f"media/cars/{instance.pk}.{ext}"

class Car(models.Model):
    name = models.CharField(max_length=32,default="")
    description = models.TextField(default="")
    price_per_day = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    image = ResizedImageField(size=[1440, 810], crop=['middle','center'], upload_to=get_car_image_path, default="")

    def __str__(self):
        return self.name

class Order(models.Model) :
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    days_for_rent = models.IntegerField(default=0)
    date = models.CharField(max_length=50, default="")

    def get_total_price(self):
        if self.car.price_per_day is None: return None
        return self.days_for_rent * self.car.price_per_day

    def __str__(self):
        return f"{self.account} & {self.car}"


class ContactMessage(models.Model):
    message = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Message from {self.account.user.username}'
