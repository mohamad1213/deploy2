from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/accounts/')
			else:
				print(form.errors)
		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('/accounts/')

# def get_random_string(length):
#     letters = string.ascii_lowercase + string.digits
#     result_str = ''.join(random.choice(letters) for i in range(length))
#     return result_str

# def lupa(req):
# 	if req.POST:
# 		user = User.objects.filter(email=req.POST['email']).first()
# 		if user is None:
# 			return redirect('/accounts/lupatidak')

# 		token = get_random_string(16)
# 		LupaPassword.objects.create(token=token, user=user)
# 		return redirect('/accounts/lupaada')
# 		print(token)
# 	return render(req, 'accounts/lupa.html')

# def lupaada(req):
# 	return render(req, 'accounts/lupaada.html')

# def lupatidak(req):
# 	return render(req, 'accounts/lupatidak.html')

# def GantiPassword(req):

# 	token = req.GET.get('token', None)
# 	if token is None:
# 		return redirect ('/accounts/lupa')

# 	if req.POST:
# 		if req.POST['password1'] != req.POST['password2']:
# 			return redirect ('/accounts/GantiPassword?token=' + token)


# 		Lp = LupaPassword.objects.filter(token=token).first()
# 		user = User.objects.get(pk=Lp.user.pk)
# 		user.set_password(req.POST['password1'])
# 		user.save()
# 		Lp = LupaPassword.objects.filter(token=token).update(is_used=True)
# 		return redirect ('/accounts')

# 	return render(req, 'accounts/GantiPassword.html')
