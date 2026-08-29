from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

import uuid

from marks.models import Grade, ProgressStudent, DIRECTIONS

from lesson.models import LANGUAGES

class AccountManager(BaseUserManager):
	def create_user(self, login, first_name, last_name, password=None):
		if not login:
			return ValueError("Users must have an login")
		
		if not first_name or not last_name:
			return ValueError("Users must have first and last names")
		
		user = self.model(
			login=login,
			first_name=first_name,
			last_name=last_name,
			password=password
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

class User(AbstractBaseUser):
	USER_ROLES = (
		("A", "Администратор"),
		("T", "Учитель"),
		("C", "Куратор"),
		("S", "Студент")
	)
	GENDER = (
		("M", "Мужской"),
		("F", "Женский")
	)
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	login = models.CharField(verbose_name="login", max_length=255, unique=True)
	generated_password = models.CharField(max_length=128, unique=True, editable=False)
	#email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	is_blocked = models.BooleanField(default=False)

	role = models.CharField(max_length=1, blank=False, choices=USER_ROLES)

	gender = models.CharField(max_length=1, blank=False, choices=GENDER)

	birth = models.CharField(max_length=10, blank=True)

	profile_picture = models.ImageField(default="profile.png", null=True, blank=True)
	banner_picture = models.ImageField(null=True, blank=True)

	about = models.CharField(max_length=120, blank=True)

	#group = models.CharField(max_length=255)
	#grade = models.IntegerField()
	
	USERNAME_FIELD = "login"
	REQUIRED_FIELDS = ["first_name", "last_name"]
	objects = AccountManager()

	def get_full_name(self):
		return self.first_name + " " + self.last_name
	
	def __str__(self):
		return self.login
	
	@property
	def is_staff(self):
		return self.staff
	
	@property
	def is_admin(self):
		return self.admin

class Student(models.Model):
	#DIRECTIONS = (
	#	("EM", "Естественно-математический"),
	#	("OG", "Общественно-гуманитарный"),
	#)

	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

	#group = models.ForeignKey(Group, on_delete=models.PROTECT, blank=True)

	grade = models.ForeignKey(Grade, on_delete=models.PROTECT, blank=False, null=False)

	#group = models.CharField(max_length=255)
	#direction = models.CharField(max_length=255, blank=True, choices=DIRECTIONS)

	#progress = models.ManyToManyField(ProgressStudent)
	progress = models.ForeignKey(ProgressStudent, on_delete=models.CASCADE)

	#periods = models.ManyToManyField(Period)

	def __str__(self):
		return self.user.first_name+" "+self.user.last_name

class Curator(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

	def __str__(self):
		return self.user.first_name+" "+self.user.last_name

class Group(models.Model):
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	name = models.CharField(max_length=255)

	curator = models.ForeignKey(Curator, on_delete=models.PROTECT)

	language = models.CharField(max_length=9, choices=LANGUAGES)

	students = models.ManyToManyField(Student, blank=True)