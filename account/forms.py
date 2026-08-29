from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from account.models import Student, Curator, User, Group, Grade

from marks.models import DIRECTIONS, ProgressStudent, ProgressPeriodStudent

import secrets, string

from transliterate import translit

class LoginForm(forms.ModelForm):
	login = forms.CharField(
		widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите логин"}),
		required=True,
		label="Логин"
	)

	password = forms.CharField(
		widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Введите пароль"}),
		required=True,
		label="Пароль"
	)

class StudentSignupForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(StudentSignupForm, self).__init__(*args, **kwargs)
		#del self.fields["password1"]
		#del self.fields["password2"]
		#self.fields["password"].help_text = None
		#self.fields["password"] = forms.CharField(widget = forms.PasswordInput(render_value=True))
		#self.fields["password"].label = "Пароль"

		self.fields["first_name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите имя"})
		self.fields["last_name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите фамилию"})
		#self.fields["login"].widget.attrs.update({"class": "form-control", "placeholder": "Введите электронную почту"})
		#self.fields["password"].widget.attrs.update({"class": "form-control", "data-toggle": "password"})

	required_css_class="required"

	#group = forms.ModelChoiceField(
	#	queryset=Group.objects.all(),
	#	widget=forms.Select(attrs={"class": "form-choice"}),
	#	required=True,
	#	label="Группа")
	
	grade = forms.ModelChoiceField(
		queryset=Grade.objects.all(),
		widget=forms.Select(attrs={"class": "form-choice"}),
		required=True,
		label="Класс")

	#direction = forms.ChoiceField(
	#	choices=DIRECTIONS,
	#	widget=forms.Select(attrs={"class": "form-choice"}),
	#	label="Направление")

	birth = forms.DateField(
		widget=forms.DateInput(attrs={"class": "form-control", "placeholder": "ДД.ММ.ГГГГ"}),
		required=False,
		label="Дата рождения"
	)

	gender = forms.ChoiceField(
		choices=User.GENDER,
		widget=forms.RadioSelect(attrs={"class": "form-checkbox"}),
		required=True,
		label="Пол")

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ["first_name", "last_name"]
		labels = {
			"first_name": "Имя",
			"last_name": "Фамилия"
		}

	#def clean(self):
	#	data = self.cleaned_data
	#	if data.get("grade") == 10 or data.get("grade") == 11:
	#		raise forms.ValidationError("Для 10-11 классов нужно указать направление.")
	#	else:
	#		return data

	@transaction.atomic
	def save(self, *args, **kwargs):
		user = super().save(commit=False)
		password = secrets.token_urlsafe(6)

		data = self.cleaned_data

		users = User.objects.filter(first_name=data["first_name"], last_name=data["last_name"])
		last = len(users)+1

		corrected_first_name = translit(data["first_name"].lower(), "ru", reversed=True)
		corrected_last_name = translit(data["last_name"].lower(), "ru", reversed=True)
		name = corrected_first_name+"_"+corrected_last_name+"_"+str(last)

		user.login = name
		user.generated_password = password
		user.set_password(password)
		user.role = "S"
		user.gender = data["gender"]
		if data["birth"]:
			user.birth = data["birth"]
		user.save()

		#studentProgressPeriod = ProgressPeriodStudent(current=True, name="").save()
		studentProgress = ProgressStudent.objects.create()

		student = Student.objects.create(user=user, grade=data["grade"], progress=studentProgress)
		group = kwargs.get("group")
		#student.group = group

		group.students.add(student)
		return user
	
class CuratorSignupForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CuratorSignupForm, self).__init__(*args, **kwargs)
		#del self.fields["password1"]
		#del self.fields["password2"]
		#self.fields["password"].help_text = None
		#self.fields["password"] = forms.CharField(widget = forms.PasswordInput(render_value=True))
		#self.fields["password"].label = "Пароль"

		self.fields["first_name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите имя"})
		self.fields["last_name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите фамилию"})
		#self.fields["email"].widget.attrs.update({"class": "form-control", "placeholder": "Введите электронную почту"})
		#self.fields["password"].widget.attrs.update({"class": "form-control", "data-toggle": "password"})

	required_css_class="required"

	birth = forms.DateField(
		widget=forms.DateInput(attrs={"class": "form-control", "placeholder": "ДД.ММ.ГГГГ"}),
		required=False,
		label="Дата рождения"
	)

	gender = forms.ChoiceField(
		choices=User.GENDER,
		widget=forms.RadioSelect(attrs={"class": "form-checkbox"}),
		required=True,
		label="Пол")

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ["first_name", "last_name"]#"password" "email": "Эл. почта"
		labels = {
			"first_name": "Имя",
			"last_name": "Фамилия"
		}

	#def clean(self):
	#	data = self.cleaned_data
	#	if data.get("grade") == 10 or data.get("grade") == 11:
	#		raise forms.ValidationError("Для 10-11 классов нужно указать направление.")
	#	else:
	#		return data

	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		password = secrets.token_urlsafe(6)

		data = self.cleaned_data

		users = User.objects.filter(first_name=data["first_name"], last_name=data["last_name"])
		last = len(users)+1

		corrected_first_name = translit(data["first_name"].lower(), "ru", reversed=True)
		corrected_last_name = translit(data["last_name"].lower(), "ru", reversed=True)
		name = corrected_first_name+"_"+corrected_last_name+"_"+str(last)

		user.login = name
		user.generated_password = password
		user.set_password(password)
		user.role = "C"
		user.gender = data["gender"]
		if data["birth"]:
			user.birth = data["birth"]
		user.save()
		curator = Curator.objects.create(user=user)
		#student.group = self.group
		#student.grade = self.grade
		#student.direction = self.direction
		return user