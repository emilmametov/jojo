from django.db import models

# Create your models here.

class Sport(models.Model):
	titlesport = models.CharField(max_length=100)
	linksport = models.CharField(max_length=250) 
	imagesport = models.ImageField(upload_to='img')
	sourcesport = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = "Sport"

	def __str__(self):
		return self.titlesport