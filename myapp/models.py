from django.db import models

# Create your models here.
class Detail(models.Model):
	gmail_id = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

	def __str__(self):
		return self.gmail_id