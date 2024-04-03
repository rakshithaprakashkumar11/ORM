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