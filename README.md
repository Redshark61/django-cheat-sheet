# A cheat sheet for django

## Main steps

### First step

Install django

```shell
pip install django
```

### Second step

Create the project

```shell
django-admin startproject PROJECT-NAME
```

### Third step

Move into that project

```shell
cd PROJECT-NAME
```

### Fourth step

Create the app wich will run the project

```shell
py manage.py startapp APP-NAME
```

## Miscellaneous

### Run the shell

```bash
py manage.py shell
```

### Run the server

```shell
py manage.py runserver
```

## How to create a database (db)

### First

Some django app use tables in the db. So before using our own, we need to create the one needed for django.

```shell
py manage.py migrate
```

### Second

You need to create _models_. A models it's a blueprint to tell the db what a table is suppose to look like. A model is a _python class_, and you create a new class (a new model) for each table you want to add.

A model is created in _APP-NAME/models.py_ like so :

```python
from django.db import models


class NAME_OF_THE_TABLE_1(models.Model):
    NAME_OF_THE_FIRST_FIELD = VALUE_OF_THE_FIRST_FIELD # (an int, a text, a long text, a date...)
    NAME_OF_THE_SECOND_FIELD = VALUE_OF_THE_SECOND_FIELD


class NAME_OF_THE_TABLE_2(models.Model):
    NAME_OF_THE_TABLE_1 = models.ForeignKey(NAME_OF_THE_TABLE_1, on_delete=models.CASCADE) # it means the second table is linked with the first one, and if we delete the first one, we also delete this one
    NAME_OF_THE_FIRST_FIELD = VALUE_OF_THE_FIRST_FIELD # (an int, a text, a long text, a date...)
    NAME_OF_THE_SECOND_FIELD = VALUE_OF_THE_SECOND_FIELD
```

For example, we want to create a db wich stores polls, so we want a table for questions, and another one for the answer :

```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

### How to indeed create the tables

When you migrate, django will look in *NAME-OF-THE-PROJECT/settings.py* and in the variable *INSTALLED_APPS*. It's a list of all the table wich needs to be created. In order to create our own django create a create a class *APP-NAMEConfig* inside of *APP-NAME/apps.py*. It's this file we need to add inside of the variable *INSTALLED_APPS*. After being added, this list should look like this :

```python
INSTALLED_APPS = [
    'APP-NAME.apps.APP-NAMEConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Nos that we added a table for our *APP-NAME*, we need to tell django we changed *INSTALLED_APPS* :

```shell
py manage.py makemigrations APP-NAME
```

Then we need to apply those changes :

```shell
py manage.py migrate
```

## Create a page, urls and templates

### How to link to urls

Inside _PROJECT-NAME/urls.py_ :

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("APP-NAME.urls"))
]
```

Where '' stands for basic url `(https://mywbesite/)` and 'admin/' for `https://mywebsite/admin`

Those paths will route to _APP-NAME/urls.py_ and will be get as follow :

```python
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
]
```

Where <int:id> mean the url is a number, and run the _view.index_ function. Similarly, empty quotes means base url and run _views.home_ function.

### How to display pages

Inside the _APP-NAME/views.py_ :

```python
def name_of_the_views(response, some_parameter):
    # Some stuff
    return render(response, "main/name_of_the_file.html", {"name_of_a_variable_in_html":the_var_itself}) # Where {} can hold variables you want to pass into you html file
```

Where _some_parameter_ is send by the _APP-NAME/urls.py_ file, in the _urlpatterns_.

### Write html

HTML need to be written into _APP-NAME/templates/APP-NAME/_. In here you can write every html you want to use.

#### Specifications

Blocks can be use if the current is used by another HTML file. You can write things in it, and overwrite it in another file :

```html
<!--In base.html-->
<title>{% block name_of_the_block %}My title{% endblock %}</title>
```

```html
<!--In home.html-->
{% extends 'main/base.html' %}
<!-- Re-use the entire base.html file-->

{% block name_of_the_block %} Another title
<!--Rewrite above the previous block-->
{% endblock %}
```

---

Variables can be use like so :

```html
<h1>My name is {{variable}}</h1>
```

Reminders : variables are passed inside the _APP-NAME/views.py_ :

```python
def name_of_the_views(response, some_parameter):
    # Some stuff
    return render(response, "main/name_of_the_file.html", {"name_of_a_variable_in_html":the_var_itself}) # Where {} can hold variables you want to pass into you html file
```

---

Loop, statement and stuff like so can be used as follow :

```html
<ul>
    {% for item in list %}
    <li>This item : {{item}}</li>
    {% endfor %}
</ul>
```

Similarly you can do the same with if :

```html
{% if condition %}
<p>This condition is true !</p>
{% else %}
<p>This condition is false</p>
{% endif %}
```
