from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings



class Product(models.Model):

   name = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   total = models.IntegerField()
   quantity = models.IntegerField()

   class Meta:
      db_table = "Product"



class Cart(models.Model):
	
	Username = models.CharField(max_length = 50)
	Product = models. CharField(max_length = 50)
	Price = models.IntegerField()
	quantity = models.IntegerField()

	class Meta:
		db_table = "Cart"


class Person(models.Model):
    name = models.CharField(max_length=96)
    phone_number = models.CharField(max_length=12)
    
    messages_received = models.IntegerField(default=0)

from django.forms import ModelForm

class SubscribeForm(ModelForm):
    class Meta:
        model = Person
        exclude = ('date_subscribed','messages_received')






class Post(models.Model):
    title= models.CharField(max_length=300)
    content= models.TextField()


class Hotel(models.Model): 
    name = models.CharField(max_length=50) 
    hotel_Main_Img = models.ImageField(upload_to='images/')


class Profile(models.Model): 
    username = models.CharField(max_length=50) 
    image = models.ImageField(upload_to='images/')



