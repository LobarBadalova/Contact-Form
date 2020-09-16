from django.db import models
from django.forms import ModelForm
# Create your models here.

class Contact(models.Model):
	fname=models.CharField(default='', max_length=100)
	lname=models.CharField(default='', max_length=100)
	#procedure=models.
	email=models.EmailField(default='')
	date=models.DateTimeField()


	def __str__(self):
		return self.fname
