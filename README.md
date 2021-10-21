# A cheat sheet for django

## First

Install django

```shell
pip install django
```

## Second

Create the project

```shell
django-admin startproject PROJECT-NAME
```

## Third

Move into that project

```shell
cd PROJECT-NAME
```

## Fourth

Create the app wich will run the project

```shell
py manage.py startapp APP-NAME
```

APP-NAME is often *main*

## Run the shell

```bash
py manage.py shell
```

## Run the server

```shell
py manage.py runserver
```

## How to link to urls

Inside *PROJECT-NAME/urls.py* :

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("APP-NAME.urls"))
]
```

Where '' stands for basic url `(https://mywbesite/)` and 'admin/' for `https://mywebsite/admin`

Those paths will route to *APP-NAME/urls.py* and will be get as follow :

```python
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
]
```

Where <int:id> mean the url is a number, and run the *view.index* function. Similarly, empty quotes means base url and run *views.home* function.

## How to display pages

Inside the *APP-NAME/views.py* :

```python
def name_of_the_views(response, some_parameter):
    # Some stuff
    return render(response, "main/name_of_the_file.html", {"name_of_a_variable_in_html":the_var_itself}) # Where {} can hold variables you want to pass into you html file
```

Where *some_parameter* is send by the *APP-NAME/urls.py* file, in the *urlpatterns*.

## Write html

HTML need to be written into *APP-NAME/templates/APP-NAME/*. In here you can write every html you want to use.

### Specifications

Blocks can be use if the current is used by another HTML file. You can write things in it, and overwrite it in another file :

```html
<!--In base.html-->
<title>{% block name_of_the_block %}My title{% endblock %}</title>
```

```html
<!--In home.html-->
{% extends 'main/base.html' %} <!-- Re-use the entire base.html file-->

{% block name_of_the_block %}
Another title <!--Rewrite above the previous block-->
{% endblock %}

```

---

Variables can be use like so :

```html
<h1>My name is {{variable}}</h1>
```

Reminders : variables are passed inside the *APP-NAME/views.py* :

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
