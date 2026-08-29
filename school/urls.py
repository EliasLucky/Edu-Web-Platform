from django.urls import path, include

from school import views as school

app_name = "school"
urlpatterns = [
    path("control/list", school.listSchool)
]
