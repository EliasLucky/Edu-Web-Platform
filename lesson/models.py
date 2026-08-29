from django.db import models

import uuid

from django.utils.text import slugify
from django.conf import settings

from django_editorjs_fields import EditorJsJSONField, EditorJsTextField

LANGUAGES = (
	("russian", "Русский"),
	("kazakh", "Казахский")
)

class Lesson(models.Model):
	class Meta:
		ordering = ["number"]

	LESSON_TYPE = (
		("Lesson", "Урок"),
		("SAU", "СОР"),
		("SAT", "СОЧ")
	)

	title = models.CharField(max_length=100)
	#subtitle = models.CharField(max_length=100, blank=True)
	number = models.IntegerField()

	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	lesson_type = models.CharField(max_length=6, choices=LESSON_TYPE)

	#slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

	content = EditorJsJSONField(
		plugins=[
			"@editorjs/paragraph",
			"@editorjs/header@2.8.8",
			"@editorjs/quote@2.7.2",
			"editorjs-alert@1.1.4",
			"editorjs-toggle-block",

			"@editorjs/list@1.9.0",
			"@editorjs/checklist@1.6.0",

			"@editorjs/image",
			"@editorjs/link",
			"@editorjs/attaches",

			"editorjs-table",

			"@editorjs/code",

			"@calumk/editorjs-columns",

			"@editorjs/marker",
			"@editorjs/inline-code",
			"@editorjs/underline",
			"editorjs-hyperlink",
			"editorjs-change-case",
			"editorjs-tooltip",
			"@sotaproject/strikethrough",
			"editorjs-text-color-plugin",

			"editorjs-text-alignment-blocktune",

			"editorjs-drag-drop@1.1.16",
			"editorjs-undo"
		],
		tools={
			"Paragraph": {
				"class": "Paragraph",
				"inlineToolbar": "true",
				"tunes": ["alignmentTune"]
			},
			"Header": {
				"class": "Header",
				"tunes": ["alignmentTune"]
			},
			"Quote": {
				"class": "Quote",
				"inlineToolbar": "true",
				"quotePlaceholder": "Enter a quote",
				"captionPlaceholder": "Quote\'s author"
			},
			"Alert": {
				"class": "Alert",
				"inlineToolbar": "true",
				"config": {
					"alertTypes": ["primary", "secondary", "info", "success", "warning", "danger"],
					"defaultType": "info",
					"messagePlaceholder": "Enter a text"
				}
			},
			"Toggle": {
				"class": "ToggleBlock",
				"inlineToolbar": "true"
			},
			"List": {
				"class": "List",
				"inlineToolbar": "true"
			},
			#"Checklist": {
			#	"class": "Checklist",
			#	"inlineToolbar": "true"
			#},
			"Image": {
				"class": "ImageTool",
				"config": {
					"endpoints": {
						"byFile": str(settings.MEDIA_ROOT),
						"byUrl": str(settings.MEDIA_URL)
					},
					"additionalRequestHeaders": [{"Content-Type": "multipart/form-data"}]
				}
			},
			"LinkTool": {
				"class": "LinkTool"
			},
			"Attaches": {
				"class": "AttachesTool",
				"config": {
					"endpoint": str(settings.MEDIA_ROOT)
				}
			},
			"Table": {
				"class": "Table",
				"inlineToolbar": "true",
				"config": {
					"rows": 2,
					"cols": 3
				}
			},
			"Code": {
				"class": "CodeTool"
			},
			"Marker": {
				"class": "Marker"
			},
			"InlineCode": {
				"class": "InlineCode"
			},
			"Underline": {
				"class": "Underline"
			},
			"Hyperlink": {
				"class": "Hyperlink"
			},
			"Strikethrough": {
				"class": "Strikethrough"
			},
			"alignmentTune": {
				"class": "AlignmentBlockTune",
				"config": {
					"default": "right",
					"blocks": {
						"Paragraph": "left",
						"Header": "center"
					}
				}
			}
		},
		i18n={
			"messages": {
				"blockTunes": {
					"delete": {
						"Delete": "Удалить"
					},
					"moveUp": {
						"Move up": "Переместить вверх"
					},
					"moveDown": {
						"Move down": "Переместить вниз"
					}
				}
			}
		},
		null = True,
		blank = True
	)

	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
	
	#def save(self, *args, **kwargs):
	#	self.slug = slugify(self.title)
	#	print(f"title: {self.title}; slug: {self.slug}; custom_slugify: {slugify(self.title)}")
	#	super(Lesson, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return f"lesson/{self.uuid}/"
	
class SummativeAssessment(models.Model):
	lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT)

	correct_answers = models.JSONField()

class Lessons(models.Model):
	lessons = models.ManyToManyField(Lesson)

	language = models.CharField(max_length=9, choices=LANGUAGES)