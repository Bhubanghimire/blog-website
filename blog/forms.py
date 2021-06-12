from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class Creation( UserCreationForm):

    class Meta:
        model = User
        fields =  ('first_name','last_name','image','email','password1','password2')