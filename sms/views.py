from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import random

# Import the models table
from sms.models import *
# Import the twilio API
from twilio.twiml.messaging_response import MessagingResponse

# Create your views here.

@csrf_exempt
def sms_response(request):
	#print(str(request))

	# Start the TwiML response
	resp = MessagingResponse()

	if request.method == "POST":
		# Add a text message
		msg = resp.message("Hello There! The App has recieved a POST request and doesn't know what to do with it! Ask Matt what to do!")

		return HttpResponse(str(resp))
	if request.method == "GET":
		UserInput = str(request.GET.get('Body'))
		UserNumber = str(request.GET.get('From'))
		# See if the number already has a session
		try:
			game = Game.objects.get(phone=UserNumber)
			msg = resp.message(determine_response(UserInput, game))
			print("\n" + UserNumber + " - " + UserInput + "\n")
			# If the User quits, don't send them the game options
			if UserInput.lower() != "q":
				sendOptions(resp)
			# Logic to check if user survives goes just under here
			# Thirst
			if game.thirst > 5:
				game.delete()
				resp.message("You died of thirst!\nGame Over")
				return HttpResponse(str(resp))
			# Distance traveled / win check
			if game.milesTraveled >= 200:
				game.delete()
				resp.message("Congradulations, you have crossed the desert!\nYou Win!!!")
				return HttpResponse(str(resp))
			# Camel's Tiredness
			if game.camelTiredness > 8:
				game.delete()
				resp.message("Your camel has died of exhaustion!\nGame Over!")
				return HttpResponse(str(resp))
			# Enemy catches up
			if game.milesTraveled - game.enemyTraveled <= 0:
				game.delete()
				resp.message("You pursuers have caught up with you! Game Over!")
				return HttpResponse(str(resp))
			return HttpResponse(str(resp))
		except:
			# No game session in database, add a new Game Session
			newGame = Game(phone = UserNumber, previous_response = UserInput)
			newGame.save()
			resp.message("Starting New Game Session! Text 'Go' to begin. Text 'Q' at any time to quit the game.")
			return HttpResponse(str(resp))

def determine_response(UserInput, game):
	input = UserInput.lower()
	if input == "q":
		game.delete()
		return "Session has been deleted"
	elif input == "go":
		output = "Welcome to the Camel Game!\nYou have stolen a camel to make your way across the Mobi Desert.\nThe natives want their camel back and are chasing you down!\nSurvive your Desert trek and out run the natives!\n"
		return output
	elif input == "hello":
		return "Hello to you, too!"
	elif input == "a":
		# Drink Water
		if game.canteen > 0:
			game.canteen -= 1
			game.thirst = 0
			if game.camelTiredness > 0:
				 game.camelTiredness -= 1
			game.enemyTraveled += 3
			game.save()
			return "You take a drink and rest for a while."
		else:
			return "Your canteen is empty. You imagine yourself as a lifeless, dry husk."
	elif input == "b":
		# Moderate Speed
                distance = random.randrange(5,13)
                game.milesTraveled += distance
                game.thirst += 1
                game.camelTiredness += 1
                game.enemyTraveled += random.randrange(7,15)
                game.save()
                oasis = random.randrange(20)
                if oasis == 10:
                        game.thirst = 0
                        game.camelTiredness = 0
                        game.canteen = 3
                        game.save()
                        return "As you travel you happen upon an oasis!\nYou fill your canteen and your stomach with water and your camel gets some much needed rest.\nYour pursuers don't stop"
                else:
                        return "Pushing forward at a moderate speed, you travel " + str(distance) + " miles.\nYour thirst increases and your camel is a little more tired.\nYour enemies continue the chase."

	elif input == "c":
		# Full Speed ahead
		distance = random.randrange(10,21)
		game.milesTraveled += distance
		game.thirst += 1
		game.camelTiredness += random.randrange(1,4)
		game.enemyTraveled += random.randrange(7,15)
		game.save()
		oasis = random.randrange(20)
		if oasis == 10:
			game.thirst = 0
			game.camelTiredness = 0
			game.canteen = 3
			game.save()
			return "As you travel you happen upon an oasis!\nYou fill your canteen and your stomach with water and your camel gets some much needed rest.\nYour pursuers don't stop"
		else:
			return "Pushing forward at full speed, you travel " + str(distance) + " miles.\nYour thirst increases and your camel is a little more tired.\nYour enemies continue the chase."
	elif input == "d":
		# Sleep
		game.camelTiredness = 0
		game.enemyTraveled += random.randrange(7,15)
		game.save()
		return "You rest for the night.\nYour camel is happy.\nYour pursuers don't stop"
	elif input == "e":
		# Check Status
		return "Miles Travelled: " + str(game.milesTraveled) + "\nEnemy Distance: " + str(game.milesTraveled - game.enemyTraveled) + "\nCamel Tiredness: " + str(game.camelTiredness) + "\nThirst: " + str(game.thirst) + "\nCanteen: " + str(game.canteen)
	else:
		return "You said \'" + UserInput + "\', Please choose one of the following:"

def sendOptions(resp):
	msg = resp.message("Your Options are:\nA. Drink Water\nB. Moderate speed\nC. Full speed\nD. Sleep\nE. Status check\nQ. Quit \n\nWhat will you do?")
	return HttpResponse(str(resp))
