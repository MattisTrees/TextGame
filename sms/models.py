from django.db import models

# Create your models here.
class Game(models.Model):
	# Phone number of the User
	phone = models.CharField('Phone Number', max_length=12)
	# User's most recent response
	previous_response = models.CharField('Last Response', max_length=160)
	# Boolean Field to determine if the game is over
	done = models.BooleanField('Game Finished', default = False)
	# Integer representing how far the player has traveled
	milesTraveled = models.IntegerField('Miles Traveled', default = 0)
	# Integer representing how far the enemy has traveled
	enemyTraveled = models.IntegerField('Enemy Traveled', default = -20)
	# Integer representing how tired the camel is
	camelTiredness = models.IntegerField('Camel Tiredness', default = 0)
	# Integer representing the thirst of the player
	thirst = models.IntegerField('Thirst', default = 0)
	# Integer representing how how much water the player has
	canteen = models.IntegerField('Canteen', default = 3)
	# Integer to represent the change of finding an oasis
	oasis = models.IntegerField('Oasis Distance', default = -1)
	class Meta:
		ordering = ['phone']

	def __str__(self):
		return str(self.id) + " : " + self.phone
