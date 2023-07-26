from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

class user(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE,default=1)

class product(models.Model):
    productname=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    photo=models.CharField(max_length=200)
    price=models.CharField(max_length=5)

class cart(models.Model):
    PRODCUT = models.ForeignKey(product, on_delete=models.CASCADE, default=1)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)
    quantity = models.CharField(max_length=10)
    date = models.DateField(max_length=10)
    total = models.CharField(max_length=50)

class rating(models.Model):
    PRODCUT = models.ForeignKey(product, on_delete=models.CASCADE, default=1)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)
    message = models.CharField(max_length=200)
    rating = models.FloatField()
    date = models.CharField(max_length=50)


class useradrres(models.Model):
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100,default=1)
    phone = models.CharField(max_length=50)
    house = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    roadname = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    adrstype = models.CharField(max_length=100)
    pincode = models.BigIntegerField()


class ordermain(models.Model):
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)
    date = models.DateField()
    Status = models.CharField(max_length=50,default="")
    amount = models.CharField(max_length=50,default="")
    useradrs = models.ForeignKey(useradrres, on_delete=models.CASCADE, default=1)

class ordersub(models.Model):
    ORDER = models.ForeignKey(ordermain, on_delete=models.CASCADE, default=1)
    PRODUCT = models.ForeignKey(product, on_delete=models.CASCADE, default=1)
    quantity = models.CharField(max_length=50)

class Bank(models.Model):
    account_no = models.CharField(max_length=50)
    IFSC = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)











