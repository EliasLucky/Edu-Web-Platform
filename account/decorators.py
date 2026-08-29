from django.shortcuts import render, redirect

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def administrator_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="login"):
	actual_decorator = user_passes_test(
		lambda u: u.role == "A",
		login_url=login_url,
		redirect_field_name=redirect_field_name
	)
	if function:
		return actual_decorator(function)
	return actual_decorator

def teacher_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="login"):
	actual_decorator = user_passes_test(
		lambda u: u.role == "T",
		login_url=login_url,
		redirect_field_name=redirect_field_name
	)
	if function:
		return actual_decorator(function)
	return actual_decorator

def curator_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="login"):
	actual_decorator = user_passes_test(
		lambda u: u.role == "C",
		login_url=login_url,
		redirect_field_name=redirect_field_name
	)
	if function:
		return actual_decorator(function)
	return actual_decorator

def student_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="login"):
	actual_decorator = user_passes_test(
		lambda u: u.role == "S",
		login_url=login_url,
		redirect_field_name=redirect_field_name
	)
	if function:
		return actual_decorator(function)
	return actual_decorator

def unathenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			group = None
			if (request.user.groups.exists()):
				group = request.user.groups.all()[0].name

			if group == "student":
				return redirect("student")
		else:
			return view_func(request, *args, **kwargs)
	
	return wrapper_func

def allowed_users(allowed_roles=[], path=""):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return redirect(path)
		return wrapper_func
	return decorator