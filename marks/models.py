from django.db import models

#from account.models import User, Student

from django.core.validators import MaxValueValidator, MinValueValidator

from lesson.models import Lesson, SummativeAssessment, Lessons

DIRECTIONS = (
	("EM", "Естественно-математический"),
	("OG", "Общественно-гуманитарный"),
)

QUARTERS = (
	("first", "Первая четверть"),
	("second", "Вторая четверть"),
	("third", "Третья четверть"),
	("fourth", "Четвертая четверть"),
)

def user_directory_path(instance, filename):
	return "user_{0}/{1}".format(instance.user.id, filename)

class AttachedFileStudent(models.Model):
	student = models.ForeignKey("account.Student", on_delete=models.PROTECT)

	lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT)

	file = models.FileField(upload_to=user_directory_path)

	uploaded_at = models.DateTimeField(auto_now_add=True)

class Subject(models.Model):
	SUBJECTS = (
		("algebra", "Алгебра"),
		("english_language", "Английский язык"),
		("biology", "Биология"),
		("history", "Всемирная история"),
		("geography", "География"),
		("geometry", "Геометрия"),
		("informatics", "Информатика"),
		("kazakh_history", "История Казахстана"),
		("kazakh_language_and_literature", "Казахский язык и литература"),
		("business", "Основы предпринимательства и бизнеса"),
		("russian_literature", "Русская литература"),
		("russian_language", "Русский язык"),
		("physics", "Физика"),
		("chemistry", "Химия"),
		("wellness", "Wellness")
	)

	name = models.CharField(max_length=30, choices=SUBJECTS)

	quarters = models.ManyToManyField("marks.Quarter")

	#quarter = models.ForeignKey("marks.Quarter", on_delete=models.PROTECT)

	#lessons = models.ManyToManyField(Lessons)

class Quarter(models.Model):
	#grade = models.ForeignKey("marks.Grade", on_delete=models.PROTECT)

	name = models.CharField(max_length=25, choices=QUARTERS)

	current = models.BooleanField(default=False)

	lessons = models.ManyToManyField(Lessons)

	#subjects = models.ManyToManyField(Subject)

class Grade(models.Model):
	number = models.PositiveIntegerField(validators=[MinValueValidator(7), MaxValueValidator(11)])

	#quarters = models.ManyToManyField(Quarter)

	subjects = models.ManyToManyField(Subject)

	direction = models.CharField(max_length=255, choices=DIRECTIONS, blank=True, null=True)

	def __str__(self):
		if self.number == 10 or self.number == 11:
			return str(self.number)+" класс. "+dict(DIRECTIONS)[self.direction]
		
		return str(self.number)+" класс"

#class Period(models.Model):
#	quarters = models.ManyToManyField(Quarter)
#
#	current = models.BooleanField(default=False)

class ProgressLatestLessonStudent(models.Model):
	student = models.ForeignKey("account.Student", on_delete=models.PROTECT)

	subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

	quarter = models.ForeignKey(Quarter, on_delete=models.PROTECT)
	
	lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT)

class ProgressSubjectStudent(models.Model):
	#student = models.ForeignKey(Student, on_delete=models.PROTECT)

	subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

	progress = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	
	final_score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)

class ProgressQuarterStudent(models.Model):
	#student = models.ForeignKey(Student, on_delete=models.PROTECT)

	quarter = models.ForeignKey(Quarter, on_delete=models.PROTECT)

	progress = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

	#current = models.BooleanField(default=False)

	subjects = models.ManyToManyField(ProgressSubjectStudent)

class ProgressPeriodStudent(models.Model):
	#student = models.ForeignKey(Student, on_delete=models.PROTECT)

	#period = models.ForeignKey(Period, on_delete=models.PROTECT)

	current = models.BooleanField(default=False)

	name = models.CharField(max_length=9, blank=False)

	quarters = models.ManyToManyField(ProgressQuarterStudent)

class ProgressStudent(models.Model):
	#student = models.ForeignKey(Student, on_delete=models.PROTECT)

	periods = models.ManyToManyField(ProgressPeriodStudent)

class ProgressSummativeAssessment(models.Model):
	student = models.ForeignKey("account.Student", on_delete=models.PROTECT)

	summative_assessment = models.ForeignKey(SummativeAssessment, on_delete=models.PROTECT)

	score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])