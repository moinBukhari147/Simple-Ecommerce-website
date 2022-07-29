from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='BlogHome'),
    path('blogpost/<int:postid>/', views.blogpost_page, name='BlogPost'),
]
