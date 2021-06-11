from django.urls import path,include
from .views import *

urlpatterns = [
   
    path('',Home,name="home"),
    path('detail/<int:id>',DetailView,name="detail"),
]
