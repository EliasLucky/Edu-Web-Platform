# Group Structure


## Groups

The education web platform was made in thought of dividing Students into groups with their own Curator. Therefore when creating new group it is required to set curator of the group and the language of the group. So the students whose native language is Russian or Kazakh languages can be separated into groups with their own curators who speak the students' language. It was made easier so students who speak Kazakh language and have problems with Russian language could understand their curator clearly.

In order to divide groups into languages the tuple `LANGUAGES` which have `("russian","kazakh")` is used.
In turn it can be improved for more international scale so groups of students can be divided by those who speak English, French, Spanish and so on.

Creation of a new group is performed through `CreateGroupForm` which is `ModelForm`.

**Fields for group are:**
- `uuid` (UUIDField) the primary key.
- `name` (CharField) The name of the group.
- `curator` (ForeignKey) Assigned curator of the group. Required in the form.
- `language` (CharField choices=LANGUAGES) The language of the group. Required in the form.
- `students` (ManyToManyField Student) The students assigned to the group.

---

More information can be found in `./group/forms.py` and in `./account/models.py`.
