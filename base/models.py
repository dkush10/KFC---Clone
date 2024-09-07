from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class fooditems(models.Model):
    name=models.CharField(max_length=100)
    foodtype=models.CharField(max_length=15)
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=500)
    category=models.CharField(max_length=100)
    image=models.ImageField(default='default.png')

class Cart(models.Model):
    image=models.ImageField(default='default.png')
    category=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=1000)
    price=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)
    totalprice=models.IntegerField(default=0)
    host=models.ForeignKey(User,on_delete=models.CASCADE)

class Checkout(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField(null=True)
    address=models.TextField(max_length=500)
    city=models.CharField(max_length=100)
    zipcode=models.IntegerField(null=True)
    country=models.CharField(max_length=100)

    payment_method=(("cod","Cash on delivery"),
             ("cc","Credit card"),
             ("upi","UPI"))
    
    payment=models.CharField(max_length=100,choices=payment_method,default="cod")
    date=models.DateField(default=datetime.date.today)
    host=models.ForeignKey(User,on_delete=models.CASCADE)

class Contact(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Phone=models.IntegerField(null=True)
    Message=models.TextField(max_length=500)
    host=models.ForeignKey(User,on_delete=models.CASCADE)



