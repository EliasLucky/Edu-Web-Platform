## Account Structure


# Account system

The web application user accounts are divided into `USER_ROLES` `("Administrator","Teacher","Curator","Student")`.
```python

```
Each user account types have different permissions and have their own web-pages they are allowed access to.

Web application uses custom account system different from the default one from Django. Each account type have its own sign up `ModelForm`. As an example, for Student account it would be `StudentSignupForm`.

User accounts do not have `EmailField`. Instead, the `login` `CharField` is used to replace that field. Therefore the web application account system is independent and self-sustained. (It was made so the Administrator accounts can create Teacher accounts. And Curator accounts can create Student accounts. Both login and password are generated.)

Fiels for User are:
- `id` (UUIDField) the primary key.
- `login` (CharField) The login is made of `first_name+"_"+last_name+"_"+len(users)` in which `len(users)` is the amount of users that have same `first_name` and `last_name` as input'd one.
- `first_name` (CharField) First Name which the backend excepts to be in Cyrillic. Required in the form.
- `last_name` (CharField) Last name which the backend excepts to be in Cyrillic. Required in the form.
- `is_active` (BooleanField)
- `is_staff` (BooleanField)
- `is_admin` (BooleanField)
- `is_superuser` (BooleanField)
- `is_blocked` (BooleanField) Special field made so an account can be blocked and revoked access to the website.
- `birth` (DateField) The birthday date. Not required.
- `gender`(CharField choices=User.GENDER) The gender (either M or F). Required in the form.
- `role` (CharField choices=User.USER_ROLES) The user role (A - Administrator, T - Teacher, C - Curator, S - Student).
- `profile_picture` (ImageField) The user profile picture. Can be null and blank.
- `banner_picture` (ImageField) The user profile banner picture. Can be null and blank.
- `about` (CharField) The user profile about.

Note: The fields `first_name` and `last_name` even though are excepted to be in Cyrillic are turned into lowercase Latin when generating `login` field.

Fields for Student are:
- `user` (OneToOneField User) Student is connected to created User.
- `grade` (ForeignKey Grade) Grade of the student.
- `progress` (ForeignKey ProgressStudent) Progress of the student. Information about `ProgressStudent` can be found in lesson-structure.md

Fields for Curator are:
- `user` (OneToOneField User) Curator is connected to created User.

More information can be found in `./account/models.py` and in `./account/forms.py`.
