from django.urls import path, include

from consultations import views as consultations

app_name = "consultations"
urlpatterns = [
    path("<uuid:uuid>", consultations.viewConsultation),
	path("control/list", consultations.listConsultation),
	path("control/create", consultations.createConsultation),
	path("control/edit/<uuid:uuid>", consultations.editConsultation),
]
