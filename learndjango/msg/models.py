from django.db import models

# Create your models here.

class sendmail(models.Model):
	sender = models.CharField(max_length=100)
	message = models.TextField(max_length=5000)
	reciever = models.CharField(max_length=50)
	#password = models.CharField(max_length=200)
	sub = models.CharField(max_length=50)
	def __str__(self):
		return self.sender
    
