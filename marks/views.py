from django.shortcuts import render

from account.models import User, Student, Curator, Group

from marks.models import ProgressPeriodStudent, Subject, ProgressLatestLessonStudent, QUARTERS

def viewMarks(request):
	p = request.GET.get("period", "")
	tab = request.GET.get("tab", "")
	subject = request.GET.get("subject", "")
	#list_lessons = request.GET.get("list", False)

	user = User.objects.get(id=request.user.id)

	try:
		user2_ = Student.objects.get(user=user)
	except:
		pass

	context = {
		"student": user2_,
		"quarters": [],
		"quarter_names": dict(QUARTERS),
		"subject_names": dict(Subject.SUBJECTS)
	}

	student = Student.objects.get(user=request.user)

	context["grade"] = student.grade.number

	period = None

	if p != "":
		for period_ in student.progress.periods.all():
			if period_.name == p:
				period = period_
		#period = student.progress.periods.get(name=p)
	else:
		for period_ in student.progress.periods.all():
			if period_.current == True:
				period = period_
		#period = student.progress.periods.get(current=True)

	for quarter in period.quarters.all():
		context["quarters"].append(quarter)

	set_quarter = None

	if tab != "":
		try:
			if tab == "quarter-first":
				quarter = student.grade.quarters.objects.all(name="first")
				quarter_progress = period.quarters.objects.all(quarter=quarter)

				set_quarter = quarter_progress
				
				for subject in quarter_progress.subjects.objects.all():
					if context[subject.subject.name] == None:
						context[subject.subject.name] = {}

					if subject == "":
						context[subject.subject.name]["subject"] = subject.subject
						context[subject.subject.name]["progress"] = subject.progress
						context[subject.subject.name]["final_score"] = subject.final_score

						current_lesson = ProgressLatestLessonStudent.objects.get(student=student, subject=subject_model, quarter=quarter)

						context[subject.subject.name]["latest_lesson"] = current_lesson.get_absolute_url()
					
			elif tab == "quarter-second":
				quarter = student.grade.quarters.objects.all(name="first")
				quarter_progress = period.quarters.objects.all(quarter=quarter)
				
				for subject in quarter_progress.subjects.objects.all():
					if context[subject.subject.name] == None:
						context[subject.subject.name] = {}

					if subject == "":
						context[subject.subject.name]["subject"] = subject.subject
						context[subject.subject.name]["progress"] = subject.progress
						context[subject.subject.name]["final_score"] = subject.final_score

						current_lesson = ProgressLatestLessonStudent.objects.get(student=student, subject=subject_model, quarter=quarter)

						context[subject.subject.name]["latest_lesson"] = current_lesson.get_absolute_url()

			elif tab == "quarter-third":
				quarter = student.grade.quarters.objects.all(name="first")
				quarter_progress = period.quarters.objects.all(quarter=quarter)
				
				for subject in quarter_progress.subjects.objects.all():
					if context[subject.subject.name] == None:
						context[subject.subject.name] = {}

					if subject == "":
						context[subject.subject.name]["subject"] = subject.subject
						context[subject.subject.name]["progress"] = subject.progress
						context[subject.subject.name]["final_score"] = subject.final_score

						current_lesson = ProgressLatestLessonStudent.objects.get(student=student, subject=subject_model, quarter=quarter)

						context[subject.subject.name]["latest_lesson"] = current_lesson.get_absolute_url()

			elif tab == "quarter-four":
				quarter = student.grade.quarters.objects.all(name="first")
				quarter_progress = period.quarters.objects.all(quarter=quarter)
				
				for subject in quarter_progress.subjects.objects.all():
					if context[subject.subject.name] == None:
						context[subject.subject.name] = {}

					if subject == "":
						context[subject.subject.name]["subject"] = subject.subject
						context[subject.subject.name]["progress"] = subject.progress
						context[subject.subject.name]["final_score"] = subject.final_score

						current_lesson = ProgressLatestLessonStudent.objects.get(student=student, subject=subject_model, quarter=quarter)

						context[subject.subject.name]["latest_lesson"] = current_lesson.get_absolute_url()

			if subject == "":
				return render(request, "marks/subjects.html", context)
		except ProgressPeriodStudent.DoesNotExist:
			pass

	if subject != "":
		quarter = None
		
		if tab == "":
			quarter = period.quarters.objects.all(current=True)
		else:
			quarter = set_quarter

		subject_model = quarter.quarter.subjects.objects.all(name=subject)

		#subject_model = Subject.objects.get(name=subject)

		#subject_progress = quarter.subjects.objects.all(subject=subject_model)

		#if list_lessons == True:
		if context["lessons"] == None:
			context["lessons"] = {}
	
		for lesson in subject_model.lessons.all():
			context["lessons"][lesson.title] = lesson
		#else:
		#	current_lesson = ProgressLatestLessonStudent.objects.get(student=student, subject=subject_model, quarter=quarter)
		#	context["lesson"] = current_lesson.lesson

		return render(request, "marks/lessons.html", context)

	return render(request, "marks/index.html", context)