from django.shortcuts import render, redirect

from account.models import Curator, User

from account.forms import CuratorSignupForm

import secrets, string

def listSchool(request):
	tab = request.GET.get("tab", "")

	context = {
		"form": {

		},
		"user_type": ""
	}

	#groups = Group.objects.all()
	#for group in groups:
	#	context["groups"].append(group)

	password = secrets.token_urlsafe(6)

	if tab == "administrator":
		return render(request, "school/index.html")
	elif tab == "curator":
		context["user_type"] = "Кураторы"
		context["user_types"] = dict(User.USER_ROLES)
		context["users"] = []
		context["genders"] = dict(User.GENDER)

		curators = Curator.objects.all()
		for curator in curators:
			container = {}
			container["account"] = curator
			container["edit_form"] = CuratorSignupForm(instance=curator.user)
			context["users"].append(curator)

		if request.method == "POST":
			form = CuratorSignupForm(request.POST)
			if form.is_valid():
				user = form.save()

				context["form"]["add_user"] = CuratorSignupForm(initial={"password": password})
				return redirect("/school/control/list?tab=curator", context)
		
		context["form"]["add_user"] = CuratorSignupForm(initial={"password": password})
		return render(request, "school/users.html", context)
	elif tab == "teacher":
		return render(request, "school/index.html")
	elif tab == "student":
		return render(request, "school/index.html")

	return render(request, "school/index.html")