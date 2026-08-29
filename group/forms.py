from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from account.models import Student, Curator, User, Group, Grade

from lesson.models import LANGUAGES

class CreateGroupForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CreateGroupForm, self).__init__(*args, **kwargs)

		self.fields["name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите название группы"})
		#del self.fields["password1"]
	#	del self.fields["password2"]
	#	self.fields["password1"].help_text = None
	#	self.fields["password1"] = forms.CharField(widget = forms.PasswordInput(render_value=True))
	#	self.fields["password1"].label = "Пароль"

	#	self.fields["first_name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите имя"})
	#	self.fields["last_name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите фамилию"})
	#	self.fields["email"].widget.attrs.update({"class": "form-control", "placeholder": "Введите электронную почту"})
	#	self.fields["password1"].widget.attrs.update({"class": "form-control", "data-toggle": "password"})

	class Meta:
		model = Group
		fields = ["name"]
		labels = {
			"name": "Название группы"
		}

	required_css_class="required"

	#group = forms.ModelChoiceField(
	#	queryset=Group.objects.all(),
	#	widget=forms.Select(attrs={"class": "form-choice"}),
	#	required=True,
	#	label="Группа")
	
	curator = forms.ModelChoiceField(
		queryset=Curator.objects.all(),
		widget=forms.Select(attrs={"class": "form-choice"}),
		required=True,
		label="Куратор")
	
	language = forms.ChoiceField(
		choices=LANGUAGES,
		widget=forms.RadioSelect(attrs={"class": "form-checkbox"}),
		required=True,
		label="Язык обучения"
	)

	#def clean(self):
	#	data = self.cleaned_data
	#	if data.get("grade") == 10 or data.get("grade") == 11:
	#		raise forms.ValidationError("Для 10-11 классов нужно указать направление.")
	#	else:
	#		return data

	#@transaction.atomic
	def save(self):
		group = super().save(commit=False)

		data = self.cleaned_data
		group.curator = data["curator"]
		group.language = data["language"]
		group.save()
		
		return group