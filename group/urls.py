from django.urls import path, include

from group import views as group

app_name = "group"
urlpatterns = [
    path("<uuid:uuid>", group.viewGroup),
	path("control/list", group.listGroup, name="list"),
	path("control/create", group.createGroup),
	path("control/edit/<uuid:uuid>", group.editGroup, name="edit"),
]
