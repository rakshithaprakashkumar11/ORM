### Ex02 Django ORM Web Application
### Date: 

### AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

### Entity Relationship Diagram

Include your ER diagram here

### DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

### PROGRAM
## Admin.py:
```
from django.contrib import admin
from.models import library,libraryAdmin
admin.site.register(library,libraryAdmin)
```

## models.py:
```
from django.db import models
from django.contrib import admin
class library(models.Model):
      serielno=models.IntegerField(primary_key=True);
      book_name=models.CharField(max_length=20);
      authorname=models.CharField(max_length=20);
      subject=models.CharField(max_length=50);
      publisher=models.CharField(max_length=10);
class libraryAdmin(admin.ModelAdmin):
      list_display=("serielno","book_name","authorname","subject","publisher");
```
## Urls.py:
```
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```
## Apps.py:
  ```
from django.apps import AppConfig


class OrmappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ormapp'

```
### OUTPUT:
![Screenshot 2024-04-03 144857](https://github.com/rakshithaprakashkumar11/ORM/assets/150994181/ad8990df-2b15-444b-9e0d-59f06915498b)

### RESULT:
Thus the program for creating a database using ORM hass been executed successfully.
