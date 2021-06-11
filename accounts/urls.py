from django.urls import path,include
from django.conf.urls import url
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('signup',Signup,name="signup"),
   url(r'^login/$',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
   url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    
]
