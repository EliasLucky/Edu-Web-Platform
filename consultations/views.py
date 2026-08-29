from django.shortcuts import render

def viewConsultation(request, uuid):
	return render(request, "marks/index.html")

def listConsultation(request):
	return render(request, "marks/index.html")

def createConsultation(request):
	return render(request, "marks/index.html")

def editConsultation(request, uuid):
	return render(request, "marks/index.html")