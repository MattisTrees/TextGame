from django.db import models

# Create your models here.
class Game(models.Model):
	phone = models.CharField('Phone Number', max_length=12)
	previous_response = models.CharField('Last Response', max_length=160)
	class Meta:
		ordering = ['phone']

	def __str__(self):
		return str(self.id) + " : " + self.phone
