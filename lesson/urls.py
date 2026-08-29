from django.urls import path, include

from lesson import views as lesson

app_name = "lesson"
urlpatterns = [
    path("<uuid:uuid>", lesson.viewLesson),
	path("control/create", lesson.createLesson),
	path("control/edit/<uuid:uuid>", lesson.editLesson),
]
