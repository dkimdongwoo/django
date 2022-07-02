from cgitb import text
from distutils.text_file import TextFile
from importlib.resources import contents
from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)
    contents = models.TextFile()
    create_date = models.DateTimeField()
