from django.shortcuts import render, redirect

from django.urls import reverse

from account.forms import StudentSignupForm

from django.contrib.auth.decorators import login_required

from account.decorators import administrator_required, curator_required

from account.models import Group, User, Curator

from lesson.models import LANGUAGES

from group.forms import CreateGroupForm

def viewGroup(request, uuid):
	return render(request, "marks/index.html")

@login_required
@curator_required
def listGroup(request):
	context = {
		"form": {

		},
		"groups": [
			
		],
		"languages": dict(LANGUAGES)
	}

	groups = Group.objects.all()
	for group in groups:
		context["groups"].append(group)

	if request.method == "POST":
		form = CreateGroupForm(request.POST)
		if form.is_valid():
			user = form.save()

			context["form"]["add_group"] = CreateGroupForm()
			return redirect("/group/control/list", context)
		
	context["form"]["add_group"] = CreateGroupForm()

	return render(request, "group/list.html", context)

def createGroup(request):
	context = {
		"form": {

		}
	}

	if request.method == "POST":
		form = StudentSignupForm(request.POST)
		if form.is_valid():
			user = form.save()

			context["form"]["add_student"] = StudentSignupForm()#initial={"password": password}
			return redirect("group/students.html", context)
		
	#password = secrets.token_urlsafe(6)
		
	context["form"]["add_student"] = StudentSignupForm()#initial={"password": password}

	return render(request, "group/students.html", context)

@login_required
#@administrator_required
@curator_required
def editGroup(request, uuid):
	context = {
		"form": {

		},
		"students": [
			
		],
		"group": {

		}
	}

	group = Group.objects.get(uuid=uuid)
	context["group"]["name"] = group.name
	students = group.students.all()
	for student in students:
		context["students"].append(student)

	if request.method == "POST":
		form = StudentSignupForm(request.POST)
		if form.is_valid():
			user = form.save(group=group)

			context["form"]["add_student"] = StudentSignupForm()
			return redirect("/group/control/edit/"+str(uuid), context)
		
	#password = secrets.token_urlsafe(6)
		
	context["form"]["add_student"] = StudentSignupForm()

	return render(request, "group/students.html", context)