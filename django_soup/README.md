# TRAIN-IT !

###### Attribution required : Fabien Furfaro (CC 4.0 BY NC ND SA)
---


Steps :
* Extract text of imageQCM with tesseract-ocr
* Extract QCM in HTML to CSV (or SQL) : Beautiful soup

In ubuntu, don't forget to add an "files.txt" in /template folder, if you want to add any text file in any folder with right-click. ! see indentation Tab in Gedit! (not merging tad and space in same class, find \t)


Django (https://docs.djangoproject.com/fr/4.0/intro/tutorial01/)
(More detail in https://developer.mozilla.org/fr/docs/Learn/Server-side/Django)
PART 1 : 
In parent directory (if not created) : django-admin startproject QCM_WEBSITE
Run the server (in the goot repertory) : python3 manage.py runserver
Go in web browser : http://127.0.0.1:8000/
Create an app (named polls) : python3 manage.py startapp polls
modify views and add urls in poll and qcm for pointer
Go in web browser : http://127.0.0.1:8000/polls

PART 2 :
create database table : python3 manage.py migrate
create modele (it's class for basis sheme) and activate its :
	python3 manage.py makemigrations polls
	python3 manage.py sqlmigrate polls 0001
	python manage.py migrate
Test API with (run Ipython) : python3 manage.py shell (exit in Ipython)
Add __str__() method in model for text visualisation
administration site (create admin) : python3 manage.py createsuperuser
go to website : "python3 manage.py runserver" and  http://127.0.0.1:8000/admin/
make poll apps editable via interface : add modele in admin file

PART 3 :
create view (web page type) in views.py.
Write real views : HttpResponse (index, HTML gabarit) or exception (Http404)
create template folder and index.html file. (render shortcut is better than httpreponse)
Make HTML link (href) relative (name in urls.py) : href="{% url 'detail' question.id %}

PART 4 :
create minimal form in htmls files : template (detail, index and result)
use generic view for each templace : URLconf correction and views.py

PART 5 :
test routine to verify fonctionnality of code. create test.py in polls folder
run test in : python3 manage.py test polls (run in ipython) "Test_Driven_Development"

PART 6 : 
static personnalisation appearance : create css file in new folder "static/polls"
in begin of html (template)  : {% load static %} <link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}">

PART 7 :
administration form personnalization : adapt admin model
copy template : django/contrib/admin/templates de .local/lib/python/site-pack/django/contrib/admin/template/admn
