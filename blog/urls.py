from django.urls import path,include
from .views import *

urlpatterns = [
   
    path('',Home,name="home"),
    path('detail/<int:id>',DetailView,name="detail"),
    path('contact/',Contact,name="contact"),
    path('about/',About,name="about"),
    path('allpost/<int:id>', Categories,name="category")
]
