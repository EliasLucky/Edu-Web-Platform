from django.shortcuts import render

def viewLesson(request, uuid):
	return render(request, "marks/index.html")

def createLesson(request):
	return render(request, "marks/index.html")

def editLesson(request, uuid):
	return render(request, "marks/index.html")