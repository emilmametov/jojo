from django.db import models

# Create your models here.
class Politics(models.Model):
	titlepol = models.CharField(max_length=100)
	linkpol = models.CharField(max_length=250) 
	imagepol = models.ImageField(upload_to='img')
	sourcepol = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = "Politics"

	def __str__(self):
		return self.titlepol