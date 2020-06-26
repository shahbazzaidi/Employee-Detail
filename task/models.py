from django.db import models

# Create your models here.

class Task(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=50)
	contact = models.IntegerField(max_length=15, default="")
	salary =  models.IntegerField()
	address = models.TextField(max_length=150)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return self.name