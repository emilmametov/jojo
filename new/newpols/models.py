from django.db import models

# Create your models here.
class News(models.Model):
	title = models.CharField(max_length=100)
	link = models.CharField(max_length=250) 
	image = models.ImageField(upload_to='img')
	source = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = "News"

	def __str__(self):
		return self.title

		