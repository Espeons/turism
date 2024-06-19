import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class SiteUser(AbstractUser):
    def __str__(self):
        return self.last_name + " " + self.first_name

class Article(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    message = models.TextField()



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    photo = models.ImageField(upload_to='static/', null=True, blank=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    STATUS = [
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default='open')





class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


class Rev(models.Model):

    nota_options = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )


    prenumele = models.CharField(max_length=40)
    nume = models.CharField(max_length=40)
    email = models.EmailField(max_length=60)
    descriere = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    excursia = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    nota = models.CharField(max_length=6, choices=nota_options, default="1")


    def __str__(self):
        return f'{self.prenumele} {self.nume}'



