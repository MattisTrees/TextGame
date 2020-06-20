from django.db import models

# Create your models here.
class Game(models.Model):
	phone = models.CharField('Phone Number', max_length=12)
	previous_response = models.CharField('Last Response', max_length=160)
