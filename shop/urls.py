from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ShopHome'),
    path('about/',views.about, name='about'),
    path('contact/', views.contactUs, name='ContactUs'),
    path('product/<int:myid>', views.productView, name='productView'),
    path('tracking/', views.tracking, name='tracking'),
    path('checkout/', views.checkout, name='checkout'),
    path('search/',views.search, name= 'search')
]
