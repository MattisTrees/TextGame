from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
			existingGame = Game.objects.get(phone=UserNumber)
			msg = resp.message(determine_response(UserInput, existingGame))
			print("\n" + UserNumber + " - " + UserInput + "\n")
			# If the User quits, don't send them the game options
			if UserInput.lower() != "q":
				sendOptions(resp)
			return HttpResponse(str(resp))
		except:
			# No game session in database, add a new Game Session
			newGame = Game(phone = UserNumber, previous_response = UserInput)
			newGame.save()
			resp.message("Starting New Game Session! Text 'Go' to begin. Text 'Q' at any time to quit the game.")
			return HttpResponse(str(resp))

def determine_response(UserInput, existingGame):
	input = UserInput.lower()
	if input == "q":
		existingGame.delete()
		return "Session has been deleted"
	elif input == "go":
		output = "Welcome to the Camel Game!\nYou have stolen a camel to make your way across the Mobi Desert.\nThe natives want their camel back and are chasing you down!\nSurvive your Desert trek and out run the natives!\n"
		return output
	elif input == "hello":
		return "Hello to you, too!"
	elif input == "a":
		# Logic goes here
		return "You chose A"
	elif input == "b":
		# Logic goes here
		return "You chose B"
	elif input == "c":
		# Logic goes here
		return "You chose C"
	elif input == "d":
		# Logic goes here
		return "You chose D"
	elif input == "e":
		# Logic goes here
		return "You chose E"
	else:
		return "You said \'" + UserInput + "\', Please choose one of the following:"

def sendOptions(resp):
	msg = resp.message("Your Options are:\nA. Drink Water\nB. Moderate speed\nC. Full speed\nD. Sleep\nE. Status check\nQ. Quit \n\nWhat will you do?")
	return HttpResponse(str(resp))
