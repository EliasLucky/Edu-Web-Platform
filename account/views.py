from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from account.decorators import student_required, unathenticated_user, allowed_users

from account.models import User, Student, Curator, Group

from account.forms import StudentSignupForm

import secrets, string

def loginAccount(request):
	if request.user.is_authenticated:
		if request.user.role == "A":
			return redirect()
		elif request.user.role == "T":
			return redirect()
		elif request.user.role == "C":
			curator = Curator.objects.get(user=request.user)
			group = Group.objects.get(curator=curator)

			return redirect("group:edit", group.uuid)
		elif request.user.role == "S":
			return redirect("/welcome")

	if request.method == "POST":
		username = request.POST["login"]
		password = request.POST["password"]
		print(password)
		print(username)

		user = authenticate(request, username=username, password=password)

		if user is not None:
			print("not none")
			login(request, user)
			if user.role == "A":
				return redirect("school")
			elif user.role == "T":
				return redirect("control/courses/list")
			elif user.role == "C":
				return redirect("/group/control/list")
			elif user.role == "S":
				return redirect("/welcome")
		else:
			messages.info(request, "Введен неверный логин или пароль")
			return redirect("/")
		
	return render(request, "account/login.html")

def logoutAccount(request):
	logout(request)

	return redirect("login")

def register(request):
	if request.method == "POST":
		form = StudentSignupForm(request.POST)
		if form.is_valid():
			user = form.save()

			context = {}
			context["form"] = StudentSignupForm()
			return render(request, "test/register.html", context)
		
	password = secrets.token_urlsafe(6)
			
	context = {}
	context["form"] = StudentSignupForm(initial={"password1": password})
	return render(request, "test/register.html", context)

def viewProfile(request, uuid):
	user = User.objects.get(id=uuid)
	try:
		user2_ = Curator.objects.get(user=user)
	except:
		pass

	try:
		user2_ = Student.objects.get(user=user)
	except:
		pass
	
	context = {
		"user_profile": user2_,
		"group_name": ""
	}

	return render(request, "account/profile.html", context)

def editProfile(request, uuid):
	return render(request, "welcome/welcome.html")

def logoutProfile(request):
	logout(request)

	return redirect("/")

@login_required
@student_required
def welcome(request):
	return render(request, "account/welcome.html")

def settings(request):
	return render(request, "account/settings.html")