from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class Creation( UserCreationForm):

    class Meta:
        model = User
        fields =  ('first_name','last_name','image','email','password1','password2')


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields =  '__all__'

class CmntForm(forms.ModelForm):

    class Meta:
        model = Comment 
        widgets = {'comment': forms.Textarea(attrs={'rows':4, 'cols':15})}
        fields = ( 'comment',)