from django.db import models
# from django.utils import timezone
# Create your models here.
class ScippetModel(models.Model):
	title=models.CharField(max_length=255)
	content=models.TextField()
	author=models.CharField(max_length=255)
	# date=models.DateField(default=timezone.now())

	# def __str__(self):
	# 	return self.title
