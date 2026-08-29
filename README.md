# Edu-Web-Platform


# Overview

Education platform made in Django. Students can complete lessons and assignments. Teachers can create new Student accounts, lessons and assignments. And much more.

The web application is divided into multiple parts.

The project is unfinished. Most of the pages are still in development. The platform architecture (database, django app structure and templates with templatetags) is completed so the project direction is clear.

# Account system

The web application user accounts are divided into `USER_ROLES` ("Administrator","Teacher","Curator","Student"). Each user account types have different permissions and have their own web-pages they are allowed access to.

User accounts also do not have `EmailField`. Instead, the login `CharField` is used to replace that field. Therefore the web application account system is independent and self-sustained. (It was made so the Administrator accounts can create Teacher accounts. And Teacher accounts can create Student accounts. Both login and password are generated.)

---

Student

# Lessons system

The education system for this platform is made in thought of Kazakhstan's Education System. There are Kazakh-medium and Russian-medium schools. The primary difference is: In Russian-medium schools the subjects "Russian Language", "Russian Literature" and "Kazakh Language and Literature" are taught. In Kazakh-medium schools the subjects "Kazakh Language", "Kazakh Literature" and "Russian Language" are taught.

To simplify the division. There is tuple `LANGUAGES` which have `("russian", "kazakh")`. The `Lesson` class itself does not have a field for said division. It's the `Lessons` class that have `ManyToManyField(Lesson)` and `language` field that uses `LANGUAGES`.

Therefore the `Lessons` class contains `Lesson`(s). It is the `Lessons` that can be divided for Kazakh-medium and Russian-medium schools.

Important note: in `Lesson` class, `LESSON_TYPE` have special types "Lesson", "Summative Assessment for the Unit (SAU)" and "Summative Assessment for the Term (SAT)". Starting from the 2026-2027 school period, SAU and SAT are no longer a thing. Therefore in the future development of this project those two types can be replaced with another one (e.g. "Test"). The `LESSON_TYPE` was made for the Lessons to have different types - basic lesson which have content and may have homework assigned, and test lesson where student have to complete a test with the knowledge he already acquired from the previous lessons.

Each Lesson in order to have something to display have `EditorJsJSONField` which uses editor.js. It was made so Teacher accounts can create new Lessons and fill it using editor.js. The `EditorJsJSONField` containts all the plugins that are allowed for editor.js.

More information can be found in `./marks/models.py` and in `./lesson/models.py`.

# Student progress

The student progress is implemented into the class `ProgressStudent` which then relates to `ProgressPeriodStudent` and `ProgressQuarterStudent` classes.

It was made so Student account type is designated a Progress which consists of Period(s) (e.g. 2025-2026, 2026-2027 and so on) which consists of Quarters.

Each Quarter in turn have `ManyToManyField` for `ProgressSubjectStudent`. Each subject has its own progress in its own quarter (which is in its own period).

Important to note that `ProgressQuarterStudent` and `ProgressSubjectStudent` have `progress = models.IntegerField`. It was made so the Quarter and Subject(s) progress can be tracked. Progress is thought of to be in percents (e.g. 100% or 63% and so on)

`ProgressLatestLessonStudent` 

More information can be found in `./marks/models.py`.

## Quickstart

- Clone the repository
  ```shell
  git clone https://github.com/EliasLucky/Edu-Web-Platform.git
  cd Edu-Web-Platform
  ```
- Install Python packages
  ```shell
  pip install -r requirements.txt
  ```

## Central Python packages

*Django* is used as a primary backed for the web application.

*Django-editorjs-fields* is a module used for Django backend to store into the database lessons made using Editor.js.

*Pillow* is used for an ImageField in the database.

## Contributing

## Can I contribute?

Yes! If you are a coder feel free to *Fork* the repository and send your amazing Pull Requests!

## How should I contribute?

Python PEP-8 code style guidelines.
JavaScript Modern ES6+ Syntax.

## Branches

- `main` - production ready codebase
- `dev` - completed but not yet released changes
