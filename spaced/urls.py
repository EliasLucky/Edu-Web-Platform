"""
URL configuration for spaced project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from account import views as account
from account import urls as profile
from lesson import urls as lesson
from marks import views as marks
from group import urls as group
from control import urls as control
from consultations import urls as consultations
from school import urls as school

urlpatterns = [
    #path('admin/', admin.site.urls),
	path("", account.loginAccount, name="login"),
	path("settings/", account.settings),
	path("profile/", include(profile, namespace="profile")),
	path("welcome/", account.welcome, name="welcome"),
	path("marks/", marks.viewMarks, name="marks"),
	path("lesson/", include(lesson, namespace="lesson")),
	path("group/", include(group, namespace="group")),
	path("courses/", include(control, namespace="courses")),
	path("consultations/", include(consultations, namespace="consultations")),
	path("school/", include(school, namespace="school")),
	#path("consultations",),
	#path("group", ),
	#path("lesson", include(lesson, namespace="lesson")),
	path("register", account.register)
]
