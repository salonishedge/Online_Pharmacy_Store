from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms

class SubscribeForm(forms.Form):
  name = forms.CharField(label='Your Name', max_length=100)
  phone_number = forms.CharField(label='Phone Number', max_length=12, min_length=10)

		


  
class UserUpdateForm(forms.ModelForm): 
  
    class Meta: 
        model = Profile
        fields = ['username', 'image'] 

class HotelForm(forms.ModelForm): 
  
    class Meta: 
        model = Hotel 
        fields = ['name', 'hotel_Main_Img'] 