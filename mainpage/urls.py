from django.contrib import admin   
from django.urls import path
from . import views

from .views import *






urlpatterns = [
    path('', views.hello,name='mainpage-hello'),

   path('about/',views.about,name='mainpage-about'),
   path('createpost/',views.createpost,name='mainpage-createpost'),
   path('hotel_images_form/',views.createpost,name='mainpage-hotel_images_form'),



   path('viewproducts/', views.viewproducts, name='mainpage-viewproducts'),

    path('aboutus/', views.aboutus, name='mainpage-aboutus'),

    path('cart/', views.cart, name='mainpage-cart'),

   path('tp/',views.tp,name='tp'),
   path('db/',views.db,name='db'),
    path('image_upload', hotel_image_view, name = 'image_upload'), 
    path('success', success, name = 'success'), 


 

]



  

  



