

#UPATE 0

# from django.shortcuts import render,redirect
# from django.contrib import messages
# from .forms import newform
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# # Create your views here.


# def register(request):
# 	form = newform(request.POST or None)
# 	if request.method == "POST":
# 		form = newform(request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')#form.cleaned_data is a dic,with all the data
# 			messages.success(request, f"Account Created :)")#gotta put this in html basic
# 			form.save()
# 			return redirect('login')
# 	return render(request,'users/register.html', {'form':form})

#END UPDATE


#update 1

from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import newform,UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def email(request):
    subject = 'Thank you for registering to our site :)'
    message = ' it  means the world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['azzzy24@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('blog-home')

def register(request):
	form = newform(request.POST or None)
	if request.method == "POST":
		form = newform(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')#form.cleaned_data is a dic,with all the data
			messages.success(request, f"Account Created :)")#gotta put this in html basic
			return redirect('login')
	return render(request,'users/register.html', {'form':form})



@login_required#user must be logged in to use it,this is a decorator, after login we are redirected to the profile page
def profile(request):
	u_form = UserUpdateForm()
	p_form = ProfileUpdateForm()
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST,
								instance=request.user)
		p_form = ProfileUpdateForm(request.POST,request.FILES,
									instance=request.user.profile)
		if u_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f"Account Created :)")#gotta put this in html basic
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	context={'u_form':u_form,'p_form':p_form}
	return render(request, 'users/profile.html', context)   