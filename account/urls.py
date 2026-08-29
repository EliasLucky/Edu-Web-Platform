from django.urls import path, include

from account import views as account

app_name = "profile"
urlpatterns = [
    path("<uuid:uuid>", account.viewProfile, name="view_profile"),
	path("control/edit/<uuid:uuid>", account.editProfile),
	path("logout/", account.logoutProfile, name="logout")
]
