'''
views.py: python functions and classes which receive web requests/http requests and return an http response


ursl.py: Redirecting urls 
    import include
    urlpatterns=[
        path('<if this url matches>',include('Redirect to here'), name="Name of that path")
    ]
#Adding __intit__.py to any directory makes it act like a python module

HttpResponse function returns an http response 

static: contains all images/html/css/misc content used 
templates: contains all the templates for the django project

models are special objects in django 
It is saved in the database

Alternate way to think of models: Like columsn and rows in a spreadsheet

Syntax to follow while creating objects in models.py:
class Name(models.Model):
models.Model means we are defining a Django Model which will be saved in the database

models.Charfield Character Limit
models.Textfield No Character Limit
models.DateTimeField
models.ForeignKey - Link to another model

Next step is to make migrations for the newly created model:
python manage.py makemigrations <app name>
python manage.py migrate vlog
This step adds the newly created model into the database





For making Model available in admin we have to register it:
admin.register.site(<Class Name>)

'''