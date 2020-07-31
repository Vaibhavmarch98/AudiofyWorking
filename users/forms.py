from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class newform(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model= User#when we do a form .save itll save it throgh the user model
		fields = ['username','email']#field we want in the form and in what order 


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']


def save(self, *args, **kwargs):
	super(Profile, self).save(*args, **kwargs)