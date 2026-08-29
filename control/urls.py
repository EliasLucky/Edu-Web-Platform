from django.urls import path, include

from control import views as control

app_name = "courses"
urlpatterns = [
    path("list", control.viewCourses)
]
