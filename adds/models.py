from django.db import models

# Create your models here.
class Food(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __str__(self):
		return self.title