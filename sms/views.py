from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
		msg = resp.message(determine_response(UserInput))
		print(UserInput)
		return HttpResponse(str(resp))


def determine_response(UserInput):
	if UserInput == "Hello":
		return "Hello to you, too!"
	else:
		return "Please say 'Hello', that's the only word I know."
