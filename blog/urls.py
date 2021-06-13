from django.urls import path,include
from .views import *

urlpatterns = [
   
    path('',Home,name="home"),
    path('detail/<int:id>',DetailView,name="detail"),
    path('c',Contact,name="contact"),
    path('a',About,name="about"),
    path('allpost/<int:id>', Categories,name="category"),
    path('post/<id>/reply',ReplyView, name="reply"),
]
