from django.shortcuts import render

from django.http.response import Http404

from marks.models import Grade, Quarter, Subject, DIRECTIONS, QUARTERS

from lesson.models import LANGUAGES

def viewCourses(request):
	subject = request.GET.get("subject", "")
	g = request.GET.get("grade", "")
	d = request.GET.get("direction", "")
	l = request.GET.get("language", "")
	q = request.GET.get("quarter", "")

	context = {}
	
	if subject != "" and g == "" and l == "" and q == "":
		context = {
			"grades": [],
			"grade_directions": dict(DIRECTIONS),
			"subject": "",
			"subject_names": dict(Subject.SUBJECTS)
		}

		try:
			subjectObject = Subject.objects.get(name=subject)
		except:
			raise Http404("Предмет не найден.")
		
		context["subject"] = subject
		
		grades = Grade.objects.all()
		for grade in grades:
			context["grades"].append(grade)

		return render(request, "control/subject.html", context)
	elif subject != "" and g != "" and l == "" and q == "":
		context = {
			"grade": None,
			"grade_directions": dict(DIRECTIONS),
			"subject": "",
			"subject_names": dict(Subject.SUBJECTS),
			"languages": dict(LANGUAGES)
		}

		try:
			subjectObject = Subject.objects.get(name=subject)
		except:
			raise Http404("Предмет не найден.")
		
		context["subject"] = subject
		
		try:
			if g == "10" or g == "11":
				gradeObject = Grade.objects.get(number=int(g), direction=d)
			else:
				gradeObject = Grade.objects.get(number=int(g))
		except:
			raise Http404("Класс не найден.")

		context["grade"] = gradeObject

		return render(request, "control/grade.html", context)
	elif subject != "" and g != "" and l != "" and q == "":
		context = {
			"grade": None,
			"grade_directions": dict(DIRECTIONS),
			"subject": "",
			"subject_names": dict(Subject.SUBJECTS),
			"language": l,
			"languages": dict(LANGUAGES),
			"quarters": [],
			"quarter_names": dict(QUARTERS)
		}

		try:
			subjectObject = Subject.objects.get(name=subject)
		except:
			raise Http404("Предмет не найден.")
		
		context["subject"] = subject
		
		try:
			if g == "10" or g == "11":
				gradeObject = Grade.objects.get(number=int(g), direction=d)
			else:
				gradeObject = Grade.objects.get(number=int(g))
		except:
			raise Http404("Класс не найден.")

		context["grade"] = gradeObject

		for quarter in subjectObject.quarters.all():
			context["quarters"].append(quarter)

		return render(request, "control/language.html", context)
	elif subject != "" and g != "" and l != "" and q != "":
		context = {
			"grade": None,
			"grade_directions": dict(DIRECTIONS),
			"subject": "",
			"subject_names": dict(Subject.SUBJECTS),
			"language": l,
			"languages": dict(LANGUAGES),
			"quarter": "",
			"quarter_names": dict(QUARTERS),
			"lessons": []
		}

		try:
			subjectObject = Subject.objects.get(name=subject)
		except:
			raise Http404("Предмет не найден.")
		
		context["subject"] = subjectObject.name
		
		try:
			if g == "10" or g == "11":
				gradeObject = Grade.objects.get(number=int(g), direction=d)
			else:
				gradeObject = Grade.objects.get(number=int(g))
		except:
			raise Http404("Предмет не найден.")
		
		context["grade"] = gradeObject

		try:
			quarter = Quarter.objects.get(name=q)
		except:
			raise Http404("Четверть не найдена.")
		
		quarterObject = None
		
		for subject_ in subjectObject.quarters.all():
			try:
				subject_.quarters.get(name=q)
			except:
				raise Http404("Четверть не найдена.")
		
		context["quarter"] = quarterObject.name

		lessons = None
		for lesson in quarterObject.lessons.all():
			if lesson.language == l:
				lessons = lesson

		for lesson in lessons:
			context["lessons"].append(lesson)

		return render(request, "control/quarter.html", context)
	
	context = {
		"subjects": [],
		"subject_names": dict(Subject.SUBJECTS)
	}

	subjects = Subject.objects.all()
	for subject in subjects:
		context["subjects"].append(subject)

	return render(request, "control/index.html", context)