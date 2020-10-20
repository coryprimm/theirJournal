from __future__ import unicode_literals
from django.db import models

# Create your models here.
class WholeEntry(models.Model): #This is the entire text entry
    title = models.TextField(max_length = 100)
    entry = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class TypeOfTag(models.Model):
    the_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TheTag(models.Model):
    content = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    wholeEntry = models.ForeignKey(WholeEntry, related_name="theTags", on_delete = models.CASCADE)
    typeOfTag = models.ForeignKey(TypeOfTag, related_name="theTypeTags", on_delete = models.CASCADE)